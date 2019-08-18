from django import forms
from .models import ExcessBaggageEnquiry, PetRelocationEnquiry, RepatirationsEnquiry


class ExcessBaggageForm(forms.ModelForm):

    class Meta:

        model = ExcessBaggageEnquiry
        fields = ['fullname', 'email', 'mobile', 'destination_country', 'destination_city', 'origin_country','origin_city', 'baggage_detail']

        widgets = {'baggage_detail': forms.HiddenInput()}
