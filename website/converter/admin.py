from django.contrib import admin

# Register your models here.
from .models import Upload, Output

admin.site.register(Upload)
admin.site.register(Output)
