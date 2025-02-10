from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'head_of_department', 'status', 'contact_email', 'phone_number', 'created_at')
    list_filter = ('status', 'head_of_department')
    search_fields = ('department_name', 'contact_email', 'phone_number')
    ordering = ('department_name',)