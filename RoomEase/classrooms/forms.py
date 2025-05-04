from django import forms
from .models import BookingRequest, CancelClass
from django.core.exceptions import ValidationError
from django.utils import timezone


class BookingRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reason'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your reason for booking this time slot...'
        })

    class Meta:
        model = BookingRequest
        fields = ['reason']
        widgets = {
            'reason': forms.Textarea(attrs={
                'rows': 4,
                'minlength': '20',
                'maxlength': '500'
            }),
        }
        labels = {
            'reason': 'Booking Reason'
        }
        help_texts = {
            'reason': 'Please provide a detailed reason for your booking request (20-500 characters)'
        }

    def clean_reason(self):
        reason = self.cleaned_data.get('reason')
        if len(reason) < 20:
            raise ValidationError("Reason must be at least 20 characters long.")
        return reason


class CancelClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reason'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Explain why this class needs to be cancelled...'
        })

    class Meta:
        model = CancelClass
        fields = ['reason']
        widgets = {
            'reason': forms.Textarea(attrs={
                'rows': 4,
                'minlength': '20',
                'maxlength': '500'
            }),
        }
        labels = {
            'reason': 'Cancellation Reason'
        }
        help_texts = {
            'reason': 'Please provide a valid reason for cancellation (20-500 characters)'
        }

    def clean_reason(self):
        reason = self.cleaned_data.get('reason')
        if len(reason) < 20:
            raise ValidationError("Cancellation reason must be at least 20 characters long.")

        # Check for inappropriate words (basic example)
        inappropriate_words = ['cancel', 'free', 'available']
        if any(word in reason.lower() for word in inappropriate_words):
            raise ValidationError("Please provide a more specific reason for cancellation.")

        return reason
