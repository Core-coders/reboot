from django.db import models

# Create your models here.


class Districdetails(models.Model):
    distid = models.IntegerField()
    distname = models.CharField(max_length=100)
    def __str__(self):
        return self.distid

class Studentdetails(models.Model):
    name = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    Schoolid = models.IntegerField(default=0)
    dob = models.DateTimeField()
    aadhar = models.IntegerField()
    slug = models.SlugField(default="test")
    def __str__(self):
        return self.name
        
class Hmdetails(models.Model):
    hmid = models.CharField(max_length=50,default="test")
    hmname = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    schoolid = models.IntegerField(default=0,primary_key=True)
    def __str__(self):
        return self.hmid