from django.contrib import admin
from .models import Tale
from .models import Content

# Register your models here.
admin.site.register(Tale)
admin.site.register(Content)