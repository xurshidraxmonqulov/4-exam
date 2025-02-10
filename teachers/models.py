from django.db import models
from django.shortcuts import reverse
from config.utils import BaseModel
from departments.models import Department
from subjects.models import Subject


class Teacher(BaseModel):
    EMPLOYMENT_TYPE_CHOICES = [
        ('full', 'Full Time'),
        ('part', 'Part Time'),
        ('contract', 'Contract'),
    ]

    STATUS_CHOICES = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
        ('pd', 'Pending'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers_images/')
    address = models.TextField()
    join_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='ac')
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='teachers', null=True, blank=True
    )
    employment_type = models.CharField(max_length=8, choices=EMPLOYMENT_TYPE_CHOICES)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        related_name='teachers', null=True, blank=True
    )

    def get_detail_url(self):
        return reverse('teachers:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_status_display()})"