from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'father_name', 'student_class', 'student_number', 'is_in_school')
    search_fields = ('last_name', 'first_name', 'father_name', 'student_number')