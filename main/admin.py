from django.contrib import admin
from .models import Department, Faculty, Student, ContactMessage

admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(ContactMessage)
