from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


# Create your models here.
class Membre(models.Model):
    CATEGORY=(
        ('Male', 'Male'),
        ('Female', 'Female')
	)
    CATEGORY1=(
        ('Active', 'Active'),
        ('desactive', 'desactive')
	)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Full_Name=models.CharField(max_length=500)
    Gender =models.CharField(max_length=50, choices=CATEGORY)
    Email=models.EmailField()
    Phone=models.CharField(max_length=25)
    account_status=models.CharField(max_length=50,choices=CATEGORY1,null=True,blank=True)
    Profile_Picture=models.ImageField(default='log.jpg', upload_to='profile_pics')
    """def __str__(self):
        return f"{self.Full_Name,self.Email}"
    def __iter__(self):
        # first start by grabbing the Class items
        iters = dict((x,y) for x,y in Membre.__dict__.items() if x[:2] != '__')
        """
    def save(self):
        super().save()
    def __str__(self):
        return str(self.Email)
class Patient(Membre):
    date_of_birth=models.DateTimeField(null=True,blank=True)
    address=models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return str(self.user)
class Doctor(Membre):
    Qualification=models.CharField(max_length=500,null=True,blank=True)
    Clinic_Map=models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return str(self.user)
class Service(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete = models.CASCADE,related_name="doctor")
    Name=models.CharField(max_length=500)
    Price=models.FloatField()
    def __str__(self):
        return self.Name
class Payment(models.Model):
    patient=models.ForeignKey(Patient,on_delete = models.CASCADE)
    payment_Date=models.DateTimeField(null=True,blank=True)
    service=models.ForeignKey(Service,on_delete = models.CASCADE)
    amount=models.FloatField()
    def __str__(self):
        return str(self.amount)
class Appointment(models.Model):
    patient=models.OneToOneField(Patient,on_delete = models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete = models.CASCADE,null=True,blank=True)
    appointment_Date=models.DateTimeField(null=True,blank=True)
    service=models.ForeignKey(Service,on_delete = models.CASCADE)
    Meeting_link=models.CharField(max_length=500)
    amount=models.ForeignKey(Payment,on_delete = models.CASCADE,null=True,blank=True)

