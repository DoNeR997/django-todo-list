from django.contrib import admin
from .models import Task
from django.contrib.auth.models import User  # ← to dodajesz

print(">>> Task model loaded and registered in admin")  # debug
admin.site.register(Task)
