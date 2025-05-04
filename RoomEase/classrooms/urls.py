from django.urls import path
from . import views

app_name = 'classrooms'

urlpatterns = [
    # Dashboard and room views
    path('', views.room_dashboard, name='dashboard'),
    path('rooms/<str:room_number>/', views.room_schedule, name='room_schedule'),

    # Booking system
    path('rooms/<str:room_number>/<str:day>/<int:time_slot_id>/book/',
         views.request_booking,
         name='request_booking'),

    # Cancellation system
    path('cancel/<int:schedule_id>/',
         views.cancel_class,
         name='cancel_class'),

    # Approval system (for staff/admin)
    path('approvals/',
         views.approval_queue,
         name='approval_queue'),
    path('approvals/booking/<int:request_id>/<str:action>/',
         views.process_booking_request,
         name='process_booking_request'),
    path('approvals/cancellation/<int:cancellation_id>/<str:action>/',
         views.process_cancellation,
         name='process_cancellation'),


]
