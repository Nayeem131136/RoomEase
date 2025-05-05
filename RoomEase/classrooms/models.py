from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.room_number


class TimeSlot(models.Model):
    slot_number = models.PositiveIntegerField(unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Slot {self.slot_number} ({self.start_time}-{self.end_time})"


class DailySchedule(models.Model):
    DAY_CHOICES = [
        ('Sun', 'Sunday'),
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Sat', 'Saturday'),
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    is_cancelled = models.BooleanField(default=False)  # New field to track cancellation status

    class Meta:
        unique_together = ('day', 'room', 'time_slot')

    def __str__(self):
        return f"{self.day} {self.time_slot}: {self.course_code} {self.section} in {self.room}"


class BookingRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DailySchedule.DAY_CHOICES)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester.username}'s request for {self.room} on {self.day} at {self.time_slot}"


class CancelClass(models.Model):
    """Model to track class cancellations"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(DailySchedule, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    cancelled_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cancellations_approved'
    )

    class Meta:
        verbose_name = "Class Cancellation"
        verbose_name_plural = "Class Cancellations"

    def __str__(self):
        return f"Cancellation request for {self.schedule} by {self.requester.username}"

    def save(self, *args, **kwargs):
        """Update the schedule's is_cancelled status when cancellation is approved"""
        if self.status == 'approved' and not self.cancelled_at:
            self.schedule.is_cancelled = True
            self.schedule.save()
            self.cancelled_at = timezone.now()
        super().save(*args, **kwargs)