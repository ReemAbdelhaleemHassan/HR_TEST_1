from django.contrib import admin
from . import models

# Register your models here.
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'date_of_birth', 'work_system', 'period_of_work', 'joining_date', 'title', 'administration')
    list_filter = ('branch', 'work_system', 'period_of_work', 'title', 'administration')
    search_fields = ('name', 'name_in_english', 'national_id', 'title', 'administration')

admin.site.register(Employee, EmployeeAdmin)


