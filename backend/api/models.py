from django.db import models

class Item(models.Model):
    first_name = models.CharField(max_length=100, default='Edcel')
    middle_name = models.CharField(max_length=100, default='Aspera')
    last_name = models.CharField(max_length=100, default='Capuyan')
    address = models.CharField(max_length=200, default='Unknown')
    zip_code = models.CharField(max_length=10, default='00000')
    email = models.EmailField(default='example@gmail.com')
    phone = models.CharField(max_length=15, default='000-000-0000')
    place_of_birth = models.CharField(max_length=100, default='Unknown')
    date_of_birth = models.DateField(default='2000-01-01')
    sex = models.CharField(max_length=10, default='Unknown')
    civil_status = models.CharField(max_length=50, default='Single')
    citizenship = models.CharField(max_length=50, default='Unknown')
    height = models.PositiveIntegerField(default=0)  
    weight = models.PositiveIntegerField(default=0)  
    blood_type = models.CharField(max_length=3, default='O+')
    occupation = models.CharField(max_length=100, default='Unemployed')
    mother_first_name = models.CharField(max_length=100, default='Unknown')
    mother_middle_name = models.CharField(max_length=100, default='Unknown')
    mother_last_name = models.CharField(max_length=100, default='Unknown')
    father_first_name = models.CharField(max_length=100, default='Unknown')
    father_middle_name = models.CharField(max_length=100, default='Unknown')
    father_last_name = models.CharField(max_length=100, default='Unknown')
    elementary = models.CharField(max_length=100, default='Unknown Elementary')
    secondary = models.CharField(max_length=100, default='Unknown High School')
    college = models.CharField(max_length=100, default='Unknown College')
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.middle_name} {self.last_name}"
