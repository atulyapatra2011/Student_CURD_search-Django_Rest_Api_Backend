from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    roll_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    gender = models.CharField(max_length=50)
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'