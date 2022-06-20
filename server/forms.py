
from django import forms
from .models import Appointment,Patient,Doctor,Membre
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Appointment_Form(forms.ModelForm):
    class Meta:
        model = Appointment
        #fields = ["doctor","appointment_Date","service","Meeting_link"]
        fields="__all__"
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
class UserForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields ='__all__'
        #fields =["Full_Name","Gender","Email","Phone","Profile_Picture","address","date_of_birth"]
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor 
        fields ='__all__'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['Profile_Picture']
