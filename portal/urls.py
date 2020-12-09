"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_views.home,name='home-page'),
    path('contact/',main_views.contact,name='contact-page'),
    path('management/',main_views.management,name='management-page'),
    path('login/',main_views.login,name='login-page'),
    path('login/pat_profile',main_views.pat_profile,name='pat_profile-page'),
    path('login/pat_profile/send_elert',main_views.send_elert,name='send_elert-page'),
    path('myadmin/',main_views.myadmin,name='myadmin-page'),
    path('myadmin/patient_reg',main_views.patient_reg,name='patient_reg-page'),
    path('myadmin/officer_reg',main_views.officer_reg,name='officer_reg-page'),
    path('myadmin/officer_reg/success_ins',main_views.success_ins,name='success_ins-page'),
    path('myadmin/patient_reg/success_pat',main_views.success_pat,name='success_pat-page'),
    path('myadmin/supplies',main_views.med_supplies,name='med_supplies-page'),
    path('myadmin/tables/ins',main_views.tables_ins,name='tables_ins-page'),
    path('myadmin/tables/pat',main_views.tables_pat,name='tables_pat-page'),
     url(r'^', include('chat.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
