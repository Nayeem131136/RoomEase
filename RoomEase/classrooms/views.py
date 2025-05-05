from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Room, TimeSlot, DailySchedule, BookingRequest, CancelClass
from .forms import BookingRequestForm, CancelClassForm


@login_required
def room_dashboard(request):
    # Get R702 room
    room = get_object_or_404(Room, room_number='R702')

    # Get today's day abbreviation (e.g., 'Mon')
    today = timezone.now().strftime('%a')

    # Get today's schedule for R702
    todays_schedule = []
    time_slots = TimeSlot.objects.all().order_by('slot_number')

    for slot in time_slots:
        try:
            schedule = DailySchedule.objects.get(
                day=today,
                room=room,
                time_slot=slot
            )
            todays_schedule.append({
                'time_slot': slot,
                'course_code': schedule.course_code,
                'section': schedule.section,
                'day': schedule.day,
                'is_booked': True,
                'is_cancelled': schedule.is_cancelled,
                'id': schedule.id
            })
        except DailySchedule.DoesNotExist:
            todays_schedule.append({
                'time_slot': slot,
                'course_code': 'Available',
                'section': '',
                'day': today,
                'is_booked': False,
                'is_cancelled': False,
                'id': None
            })

    return render(request, 'dashboard.html', {
        'room': room,
        'todays_schedule': todays_schedule,
        'today': timezone.now()
    })


@login_required
def room_schedule(request, room_number):
    room = get_object_or_404(Room, room_number=room_number)
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Sat']
    time_slots = TimeSlot.objects.all().order_by('slot_number')

    # Create a schedule grid
    schedule_grid = {}
    for day in days:
        schedule_grid[day] = {}
        for slot in time_slots:
            try:
                schedule = DailySchedule.objects.get(day=day, room=room, time_slot=slot)
                schedule_grid[day][slot.slot_number] = {
                    'schedule': schedule,
                    'is_cancelled': schedule.is_cancelled
                }
            except DailySchedule.DoesNotExist:
                schedule_grid[day][slot.slot_number] = None

    return render(request, 'classrooms/room_schedule.html', {
        'room': room,
        'days': days,
        'time_slots': time_slots,
        'schedule_grid': schedule_grid,
    })


@login_required
def request_booking(request, room_number, day, time_slot_id):
    room = get_object_or_404(Room, room_number=room_number)
    time_slot = get_object_or_404(TimeSlot, pk=time_slot_id)

    # Check if slot is already booked and not cancelled
    existing_booking = DailySchedule.objects.filter(
        day=day,
        room=room,
        time_slot=time_slot,
        is_cancelled=False
    ).exists()

    if existing_booking:
        messages.warning(request, 'This time slot is already booked!')
        return redirect('room_schedule', room_number=room_number)

    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking_request = form.save(commit=False)
            booking_request.requester = request.user
            booking_request.room = room
            booking_request.day = day
            booking_request.time_slot = time_slot
            booking_request.save()
            messages.success(request, 'Booking request submitted successfully!')
            return redirect('room_schedule', room_number=room_number)
    else:
        form = BookingRequestForm()

    return render(request, 'classrooms/request_booking.html', {
        'form': form,
        'room': room,
        'day': day,
        'time_slot': time_slot,
    })


@login_required
def cancel_class(request, schedule_id):
    schedule = get_object_or_404(DailySchedule, pk=schedule_id)

    if request.method == 'POST':
        form = CancelClassForm(request.POST)
        if form.is_valid():
            cancellation = form.save(commit=False)
            cancellation.requester = request.user
            cancellation.schedule = schedule
            cancellation.save()

            messages.success(request, 'Cancellation request submitted for approval')
            return redirect('room_schedule', room_number=schedule.room.room_number)
    else:
        form = CancelClassForm()

    return render(request, 'classrooms/confirm_cancel.html', {
        'form': form,
        'schedule': schedule
    })


@login_required
def approval_queue(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    pending_bookings = BookingRequest.objects.filter(status='pending')
    pending_cancellations = CancelClass.objects.filter(status='pending')

    return render(request, 'classrooms/approval_queue.html', {
        'pending_bookings': pending_bookings,
        'pending_cancellations': pending_cancellations
    })


@login_required
def process_booking_request(request, request_id, action):
    if not request.user.is_staff:
        return redirect('dashboard')

    booking_request = get_object_or_404(BookingRequest, pk=request_id)

    if action == 'approve':
        # Create the schedule if approved
        DailySchedule.objects.create(
            day=booking_request.day,
            room=booking_request.room,
            time_slot=booking_request.time_slot,
            course_code=booking_request.reason[:20],  # Using reason as course code for demo
            section='A'  # Default section
        )
        booking_request.status = 'approved'
        booking_request.save()
        messages.success(request, 'Booking approved successfully')
    elif action == 'reject':
        booking_request.status = 'rejected'
        booking_request.save()
        messages.success(request, 'Booking request rejected')

    return redirect('approval_queue')


@login_required
def process_cancellation(request, cancellation_id, action):
    if not request.user.is_staff:
        return redirect('dashboard')

    cancellation = get_object_or_404(CancelClass, pk=cancellation_id)

    if action == 'approve':
        cancellation.status = 'approved'
        cancellation.cancelled_by = request.user
        cancellation.schedule.is_cancelled = True
        cancellation.schedule.save()
        cancellation.save()
        messages.success(request, 'Cancellation approved successfully')
    elif action == 'reject':
        cancellation.status = 'rejected'
        cancellation.save()
        messages.success(request, 'Cancellation request rejected')

    return redirect('approval_queue')