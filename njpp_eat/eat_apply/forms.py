from django import forms
from django.forms.extras import widgets

from .models import Application, Child, Adult

# This is the form that collects all the information about a given filer. This is Step 4 on the paper form.
class ApplicationFormFilerInfo(forms.Form):
    contact_name_of_filer = forms.CharField(label="Your Full Name", max_length=200)
    no_address = forms.BooleanField(label="I do not have a permanent address", required=False)
    contact_address_one = forms.CharField(label="Street address", max_length=200, required=False)
    contact_address_two = forms.CharField(label="Apartment Number, Suite, etc.", max_length=200, required=False)
    contact_city = forms.CharField(label="City", max_length=50, required=False) # as far as I can find no US city has name longer than 24 chars
    contact_state = forms.CharField(label="State (two characters)", max_length=2, required=False)
    contact_zip = forms.CharField(label="Zip code",max_length=10, required=False)
    contact_phone = forms.CharField(max_length=10, required=False)
    contact_email = forms.EmailField(required=False)
    contact_signature = forms.CharField(label="Please enter your full name below to sign.")

# This is the form that collects 
class ApplicationFormPathSelection(forms.Form):
	assitance_choices = ((False, 'No'),(True, 'Yes'))
	foster_choices = ((False, 'No'),(True, 'Yes'))
	participate_assistance = forms.BooleanField(label="Are any members of your household participants in one or more of the following assistance programs: SNAP, TANF, or FDPIR?", widget=forms.RadioSelect(choices=assitance_choices, attrs={'class=': 'form_field radio_field'}))
	foster_children = forms.BooleanField(label="Are ALL of the children you are applying for foster children?", widget=forms.RadioSelect(choices=foster_choices, attrs={'class=': 'form_field radio_field'}))
    