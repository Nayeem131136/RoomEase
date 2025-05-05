from django.contrib import admin
from .models import Room, TimeSlot, DailySchedule, BookingRequest

admin.site.register(Room)
admin.site.register(TimeSlot)
admin.site.register(DailySchedule)
admin.site.register(BookingRequest)