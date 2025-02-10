from django.db import models
from django.core.validators import RegexValidator
from django.shortcuts import reverse
from config.utils import BaseModel


class Department(BaseModel):
    STATUS_CHOICES = [
        ('a', 'Active'),
        ('i', 'Inactive'),
        ('c', 'Closed'),
    ]

    HEAD_DEPARTMENT = [
        ('JA', 'Dr. John Anderson'),
        ('EC', 'Dr. Emily Carter'),
        ('MT', 'Dr. Michael Thompson'),
        ('SM', 'Dr. Sarah Mitchell'),
        ('DW', 'Dr. David Wilson'),
    ]

    phone_regex = RegexValidator(
        regex=r'^\+?\d{7,15}$',
        message="Telefon raqami faqat raqamlardan iborat bo‘lishi"
                " va 7-15 ta belgidan oshmasligi kerak."
    )

    department_name = models.CharField(max_length=200)
    head_of_department = models.CharField(max_length=2, choices=HEAD_DEPARTMENT)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')
    descriptions = models.TextField()
    location = models.TextField()
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, validators=[phone_regex])

    def get_detail_url(self):
        return reverse('departments:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('departments:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('departments:delete', args=[self.pk])

    def __str__(self):
        return f"{self.department_name} - {self.get_status_display()}"