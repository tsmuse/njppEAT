from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.forms import widgets
from django.forms.models import inlineformset_factory
from django.utils import timezone
from formtools.wizard.views import SessionWizardView

from .models import Application, Child, Adult
from . import forms

# Create your views here.
class IndexView(generic.FormView):
	template_name = "eat_apply/index.html"
	form_class = forms.ApplicationFormFilerInfo


class ApplicationWizard(SessionWizardView):
	template_name = "eat_apply/wizard.html"
	
	def done(self, form_list, **kwargs):
		return render_to_response('eat_apply/done.html',{
			'form-data': [form.cleaned_data for form in form-list],
			})