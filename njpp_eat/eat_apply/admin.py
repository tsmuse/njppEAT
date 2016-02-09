from django.contrib import admin
from .models import Application, Child, Adult
# Register your models here.

admin.site.register(Application)
admin.site.register(Child)
admin.site.register(Adult)