from django.db import models

# Create your models here.
class Hmdetails(models.Model):
    hmid = models.CharField(max_length=50,default="test")
    hmname = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    def __str__(self):
        return self.hmid

class Studentdetails(models.Model):
    name = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    dob = models.DateTimeField()
    aadhar = models.IntegerField()