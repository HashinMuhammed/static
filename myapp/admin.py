from django.contrib import admin

from . models import travelers
from . models import teams

# Register your models here.
admin.site.register(travelers)
admin.site.register(teams)