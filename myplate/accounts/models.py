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
    height = models.FloatField(default=1)
    weight = models.FloatField(default=0)
    bmi = models.FloatField(default=0)
    deficency = models.TextField(default="NA")
    Schoolid = models.IntegerField(default=0)
    dob = models.DateField()
    aadhar = models.IntegerField(default=0)
    status = models.TextField(default="healthy")
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

class Billupload(models.Model):
        thumb = models.ImageField(default='default.png',blank=True)

class Menu(models.Model):
    day = models.CharField(max_length=50)
    dish1 = models.CharField(max_length=50)
    dish2 = models.CharField(max_length=50)
    dish3 = models.CharField(max_length=50)
    dish4 = models.CharField(max_length=50)
    def __str__(self):
        return self.day