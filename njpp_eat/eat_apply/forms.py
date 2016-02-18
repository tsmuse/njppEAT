from django import forms
from django.forms import formset_factory
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

# This is the form that collects the information we're using to route people through the fork in the logic. If the answer is yes to either of these
# questions than the route is the "short path." foster_children is initially hidden and only shown if participate_assistance == True. 
class ApplicationFormPathSelection(forms.Form):
	assitance_choices = ((False, 'No'),(True, 'Yes'))
	foster_choices = ((False, 'No'),(True, 'Yes'))
	participate_assistance = forms.BooleanField(label="Are any members of your household participants in one or more of the following assistance programs: SNAP, TANF, or FDPIR?", widget=forms.RadioSelect(choices=assitance_choices, attrs={'class=': 'form_field radio_field'}))
	foster_children = forms.BooleanField(label="Are ALL of the children you are applying for foster children?", widget=forms.RadioSelect(choices=foster_choices, attrs={'class=': 'form_field radio_field'}))
    
# This is the form to create a Child object in the short path. It doesn't collect any income information because none is required on that path
class ChildNoIncomeForm(forms.Form):
    student_choices = ((False, 'No'), (True, 'Yes'))
    foster_choices = ((False, 'No'), (True, 'Yes'))
    homeless_choices = ((False, 'No'), (True, 'Yes'))

    child_first_name = forms.CharField(label="First Name", max_length=100)
    child_middle_initial = forms.CharField(label="Middle Initial", max_length=1, required=False)
    child_last_name = forms.CharField(label="Last Name", max_length=100)
    child_student = forms.BooleanField(label="Is this child a student?", widget=forms.RadioSelect(choices=student_choices))
    child_foster = forms.BooleanField(label="Is this child a foster child?", widget=forms.RadioSelect(choices=foster_choices))
    child_homeless = forms.BooleanField(label="Is this child homeless, a migrant, or a runaway?", widget=forms.RadioSelect(choices=homeless_choices))

application_short_path_formset = formset_factory(ChildNoIncomeForm)