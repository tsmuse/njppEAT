from django.conf.urls import url
from . import views

app_name = 'eat_apply'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]