from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import Appointment_Form,UserRegisterForm,UserForm,ProfileUpdateForm
from django.contrib import messages
from .models import Appointment,Patient,Doctor,Membre,Appointment,Service,Payment
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.models import model_to_dict
# Create your views here.
def home(request):
    patients=Patient.objects.all()
    doctors=Doctor.objects.all()
    appointment=Appointment.objects.all()
    service=Service.objects.all()
    membre_doctor=False
    membre_patient=False
    try:
        instance = Patient.objects.get(user=request.user)# EXAMPLE
        instance_dict = {key: getattr(instance, key) for key in model_to_dict(instance).keys()}
        #print(1, instance_dict.get("user"))
        if instance_dict.get("user") == request.user:
            membre_patient=True
        else:
            membre_doctor=False
    except Patient.DoesNotExist:
        instance = Doctor.objects.get(user=request.user) # EXAMPLE
        instance_dict = {key: getattr(instance, key) for key in model_to_dict(instance).keys()}
        if instance_dict.get("user") == request.user:
            membre_doctor=True
        else:
            membre_doctor=False
    except Doctor.DoesNotExist:
        membre_patient=True
    #print("hhhh",str(instance))
    print(request.user)
    print(len(patients))
    return render(request,'server/home.html',{'patient_nombre':len(patients),'appointment_nombre':len(appointment),'service_nombre':len(service),"ins":instance,"membre_patient":membre_patient,"membre_doctor":membre_doctor})
@login_required
def StartAppointment(request):
    apointments=Appointment.objects.values("amount","patient","appointment_Date","Meeting_link","service","amount")
    doctor=Doctor.objects.all()
    service=Service.objects.all()
    instance = Patient.objects.get(user=request.user)
    for i in apointments:
        amount=Payment.objects.get(id=i.get("amount"))
       
    if request.method=="POST":
        patient=Patient.objects.all()
        current_user = request.user
        apointment=Appointment_Form(request.POST)
        if apointment.is_valid():
            apointment.save()
            apointment=Appointment_Form()
            messages.success(request, f'Your Account Has Been Created ')
        else:
            messages.error(request, f"erroe")
            print(apointment.errors)
    return render(request, 'server/Appointment.html',{"apointment": Appointment_Form,"amount": amount,"doctor":doctor,"service":service,"instance":instance})
@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user)
        profile_form = UserForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
        else:
            messages.error(request, ('Please correct the error below.'))
    print(request.user)
    return render(request,'server/profile.html',{'p_form': ProfileUpdateForm,'profile_form': UserForm})


def register(request):
    if request.method == 'POST':
        current_user = request.user
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        else:
            print(form.errors)
    else:
        current_user = request.user
        form = UserRegisterForm(request.POST)
    return render(request, 'server/register.html', {'form': form,"current_user":current_user})
@login_required
def Appointment_list(request):
    patient=Patient.objects.values("Full_Name")
    apointments=Appointment.objects.values("amount","patient","appointment_Date","Meeting_link","service","amount")
    services=Service.objects.values("Name")
    membre_doctor=False
    membre_patient=False
    try:
        instance = Doctor.objects.get(user=request.user) # EXAMPLE
        instance_dict = {key: getattr(instance, key) for key in model_to_dict(instance).keys()}
        if instance_dict.get("user") == request.user:
            membre_doctor=True
        else:
            membre_doctor=False
            
    #list_results=list(zip(apointments, services))
    #print(list_results)
    #print(apointments)
    except Doctor.DoesNotExist:
        membre_patient=True
    for i in apointments:
        patient=Patient.objects.get(id=i.get("patient"))
        service=Service.objects.get(id=i.get("service"))
        appointment_Date=i.get("appointment_Date")
        amount=Payment.objects.get(id=i.get("amount"))
        meets=i.get("Meeting_link")

        print(i.get("appointment_Date"))

    return render(request, 'server/appointment_list.html', {"meets":meets,"service":service,"amount":amount,"appointment_Date":appointment_Date,"patient":patient,"membre_patient":membre_patient,"membre_doctor":membre_doctor})

