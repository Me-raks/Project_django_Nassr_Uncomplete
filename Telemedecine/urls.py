"""Telemedecine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from server.views import home,StartAppointment,Appointment_list,register,profile,Doctor_List,Patient_List
from django.contrib import admin
from django.urls import re_path as url
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #path('', include('django.contrib.auth.urls')),
    path('start_appointment', StartAppointment, name='start_appointment'),
    path('Appointment', Appointment_list, name='Appointment'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='server/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='server/logout.html'), name='logout'),
     path('api/patient', Patient_List,name='Patient_List'),
    path('api/doctor', Doctor_List,name='Doctor_List'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
