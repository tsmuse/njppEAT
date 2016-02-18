from django.conf.urls import url
from . import views, forms

app_name = 'eat_apply'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^wizard/$',views.ApplicationWizard.as_view([forms.ApplicationFormFilerInfo, forms.ApplicationFormPathSelection, forms.application_short_path_formset]))
]