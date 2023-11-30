from django.db import models

# Create your models here.

# employees/models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    
    # Address Details
    address_details = models.JSONField(default=dict)

    # Work Experience
    work_experience = models.JSONField(default=list)
    
    # Qualifications
    qualifications = models.JSONField(default=list)
    
    # Projects
    projects = models.JSONField(default=list)

    def __str__(self):
        return self.name
