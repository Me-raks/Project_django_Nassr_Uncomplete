from django.contrib import admin

from .models import Doctor,Patient,Service,Appointment,Payment,Membre
# Register your models here.

@admin.register(Membre)
class Membres(admin.ModelAdmin):
    list_display = ("Full_Name","Email")
@admin.register(Doctor)
class Doctors(admin.ModelAdmin):
    list_display = ("Full_Name", "Qualification")
@admin.register(Patient)
class Patients(admin.ModelAdmin):
    list_display = ("Full_Name","Gender")
@admin.register(Service)
class Services(admin.ModelAdmin):
    list_display = ("doctor", "Name", "Price")
@admin.register(Appointment)
class Appointments(admin.ModelAdmin):
    list_display = ("patient", "service","Meeting_link")
@admin.register(Payment)
class Payments(admin.ModelAdmin):
    list_display = ("patient", "payment_Date","service")
