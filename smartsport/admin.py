from django.contrib import admin

# Register your models here.
from smartsport.models import Series, Tournament

admin.site.register(Series)
admin.site.register(Tournament)