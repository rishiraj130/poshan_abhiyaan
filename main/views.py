import os
import uuid
import requests
import numbers
from twilio.rest import Client
from django.shortcuts import render,redirect
from officer.models import Officer
from patient.models import Patient
from .models import Dose, Medicine
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home(request):
    return render(request,'main/home.html')

def send_elert(request):
    if request.method == "POST":
        id = request.POST.get('id')
        temp = Patient.objects.get(patient_id=int(id),status=True)
        test = f'Dear {temp.first_name} {temp.last_name}.You have not taken your dose.Kindly report to the hospital.'
        phone = temp.phone

        #account_sid = 'ACa30a29dd5673c985ef9b22bf1adc4c30'
        #auth_token = 'b9614db0ee6c1bb65f17f77db114d061'
        #client = Client(account_sid, auth_token)
        #message = client.messages.create(
                    # body=message,
                    # from_='+12015791172',
                    # to='+919473456052'
                 #)
        #print(message.sid)
        context = {
           'pat' : Patient.objects.get(patient_id=int(id),status=True),
           'doses' : Dose.objects.filter(patient=int(id)),

        }
        url = "https://www.fast2sms.com/dev/bulk"
        payload = f'sender_id=FSTSMS&message={test}&language=english&route=p&numbers={phone}'
        payload = payload
        headers = {
        'authorization': "7MWvQEdTG1HjyxUmwsCutnB2hoq6LJ5eOS0Ic4Nla3KP8brYipFeYoLVwrfBkUv85qgS2xmOcpRzNEWD",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        return render(request,'main/pat_profile.html',context)


def pat_profile(request):
    if request.method == "POST":
        dose_status = request.POST.get('dose')
        dod = request.POST.get('DOD')
        patient_id = request.POST.get('id')

        patient = Patient.objects.get(patient_id=int(patient_id),status=True)

        d = Dose(date_of_dose=dod,status=dose_status,patient=patient)
        d.save()

        context = {
           'pat' : Patient.objects.get(patient_id=int(patient_id),status=True),
           'doses' : Dose.objects.filter(patient=int(patient_id))
        }
        return render(request,'main/pat_profile.html',context)
    if request.method == "GET":
        id = request.GET.get('id')
        context = {
           'pat' : Patient.objects.get(patient_id=int(id),status=True),
           'doses' : Dose.objects.filter(patient=int(id))
        }
        return render(request,'main/pat_profile.html',context)


def login(request):
    if request.method == "POST":
        ln = request.POST.get('ln')
        try:
            off = Officer.objects.get(login_number=ln)
        except Officer.DoesNotExist:
            context = {
                'error' : True
            }
            return render(request,'main/login.html',context)
        no = off.officer_id
        new_patients = Patient.objects.filter(medical_instructor=int(no),status=True)
        new_count = len(Patient.objects.filter(medical_instructor=int(no),status=True))
        context = {
            'officer' : off,
            'count' : new_count,
            'patients' : new_patients
            }
        return render(request,'main/ins_profile.html',context)




    if request.method == "GET":

        id = request.GET.get('id')
        pat = request.GET.get('pat')
        if pat is not None:
            patient = Patient.objects.get(patient_id=int(pat))
            patient.status = False
            patient.save()
            count = len(Patient.objects.filter(medical_instructor=int(patient.medical_instructor.officer_id),status=True))
            if count < 2:
                officer = Officer.objects.get(officer_id=int(patient.medical_instructor.officer_id))
                officer.aval = True
                officer.save()

        if id is not None:
            no = id[6:]
            new_officer = Officer.objects.get(officer_id=int(no))
            new_patients = Patient.objects.filter(medical_instructor=int(no),status=True)
            new_count = len(Patient.objects.filter(medical_instructor=int(no),status=True))
            context = {
                'officer' : new_officer,
                'count' : new_count,
                'patients' : new_patients
            }
            return render(request,'main/ins_profile.html',context)


    context = {'error': False}

    return render(request,'main/login.html',context)

def myadmin(request):
    nop = len(Patient.objects.all())
    nomi = len(Officer.objects.all())
    active_patients = len(Patient.objects.filter(status=True))
    aval_hi = len(Officer.objects.filter(aval=True))

    jan_pat = len(Patient.objects.filter(date_of_reg__month=1))
    feb_pat = len(Patient.objects.filter(date_of_reg__month=2))
    march_pat = len(Patient.objects.filter(date_of_reg__month=3))
    april_pat = len(Patient.objects.filter(date_of_reg__month=4))
    may_pat = len(Patient.objects.filter(date_of_reg__month=5))
    jun_pat = len(Patient.objects.filter(date_of_reg__month=6))
    july_pat = len(Patient.objects.filter(date_of_reg__month=7))
    aug_pat = len(Patient.objects.filter(date_of_reg__month=8))
    sep_pat = len(Patient.objects.filter(date_of_reg__month=9))
    oct_pat = len(Patient.objects.filter(date_of_reg__month=10))
    nov_pat = len(Patient.objects.filter(date_of_reg__month=11))
    dec_pat = len(Patient.objects.filter(date_of_reg__month=12))


    context = {
        'nop' : nop,
        'nomi' : nomi,
        'active_patients' : active_patients,
        'aval_hi' : aval_hi,
        'jan_pat': jan_pat,
        'feb_pat' : feb_pat,
        'march_pat': march_pat,
        'april_pat': april_pat,
        'may_pat': may_pat,
         'jun_pat':jun_pat,
         'july_pat':july_pat,
         'aug_pat':aug_pat,
         'sep_pat':sep_pat,
         'oct_pat':oct_pat,
         'nov_pat':nov_pat,
         'dec_pat':dec_pat

    }
    return render(request,'main/admin.html',context)

def patient_reg(request):
    context = {
          'officers': Officer.objects.filter(aval='True')
    }
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        relation   = request.POST.get('relation')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        aadhaar_number = request.POST.get('aadhaar_number')
        blood_group = request.POST.get('blood-group')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        cat = request.POST.get('cat')
        pic = request.FILES['pic']
        hist = request.POST.get('hist')
        mt = request.POST.get('mt')

        medical_intructor = Officer.objects.get(officer_id=mt)

        patient = Patient(first_name=first_name,last_name=last_name,relation=relation,date_of_birth=date_of_birth,phone=phone_number,aadhaar=aadhaar_number,blood_group=blood_group,category=cat,height=height,weight=weight,p_image=pic,registration_history=hist,medical_instructor=medical_intructor)
        patient.save()

        print(patient.date_of_reg.month)

        off_id = medical_intructor.officer_id
        off_fname = medical_intructor.first_name
        off_lname = medical_intructor.last_name

        test = f'You have been assigned {off_fname} {off_lname} with id POSMED{off_id}'
        phone = patient.phone


        #account_sid = 'ACa30a29dd5673c985ef9b22bf1adc4c30'
        #auth_token = 'b9614db0ee6c1bb65f17f77db114d061'
        #client = Client(account_sid, auth_token)
        #message = client.messages.create(
                     #body=message,
                     #from_='+12015791172',
                    # to='+919473456052'
                #)
        #print(message.sid)

        url = "https://www.fast2sms.com/dev/bulk"
        payload = f'sender_id=FSTSMS&message={test}&language=english&route=p&numbers={phone}'
        payload = payload
        headers = {
        'authorization': "7MWvQEdTG1HjyxUmwsCutnB2hoq6LJ5eOS0Ic4Nla3KP8brYipFeYoLVwrfBkUv85qgS2xmOcpRzNEWD",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)

        return redirect('success_pat-page')





    return render(request,'main/patient.html',context)

def officer_reg(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        aadhaar_number = request.POST.get('aadhaar_number')
        gender = request.POST.get('gender')
        pic = request.FILES['pic']
        degree = request.POST.get('degree')



        off = Officer(first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,phone=phone_number,gender=gender,o_image=pic,aadhaar=aadhaar_number,degree=degree)
        off.save()
        stringLength = 6

        randomString = uuid.uuid4().hex # get a random string in a UUID fromat
        randomString  = randomString.upper()[0:stringLength] # convert it in a uppercase letter and trim to your size.


        randomString = uuid.uuid4().hex
        randomString  = randomString.lower()[0:stringLength]
        randomString  += str(off.officer_id)
        off.login_number = randomString
        off.save()


        off_id = off.officer_id
        phone = off.phone


        test = f'Thank you for registering to Poshan Abhiyaan.Your id is POSMED{off_id}. Your login number is {randomString}'


        #account_sid = 'ACa30a29dd5673c985ef9b22bf1adc4c30'
        #auth_token = 'b9614db0ee6c1bb65f17f77db114d061'
        #client = Client(account_sid, auth_token)
        #message = client.messages.create(
                     #body=message,
                     #from_='+12015791172',
                     #to='+919473456052'
                 #)
        #print(message.sid)
        url = "https://www.fast2sms.com/dev/bulk"
        payload = f'sender_id=FSTSMS&message={test}&language=english&route=p&numbers={phone}'
        payload = payload
        headers = {
        'authorization': "7MWvQEdTG1HjyxUmwsCutnB2hoq6LJ5eOS0Ic4Nla3KP8brYipFeYoLVwrfBkUv85qgS2xmOcpRzNEWD",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)

        return redirect('success_ins-page')



    return render(request,'main/inspector.html')

@csrf_exempt
def med_supplies(request):
    if request.method == "POST":
        data1 = request.POST['riboflavin']
        data2 = request.POST['pyridoxine']
        data3 = request.POST['cobalamin']
        data4 = request.POST['ascorbate']
        data5 = request.POST['cholecalciferol']
        r = Medicine.objects.get(name="Riboflavin")
        r.quantity = data1
        r.save()
        p = Medicine.objects.get(name="Pyridoxine")
        p.quantity = data2
        p.save()
        c1 = Medicine.objects.get(name="Cobalamin")
        c1.quantity = data3
        c1.save()
        a = Medicine.objects.get(name="Ascorbate")
        a.quantity = data4
        a.save()
        c2 = Medicine.objects.get(name="Cholecalciferol")
        c2.quantity = data5
        c2.save()



    r_quan = Medicine.objects.get(name="Riboflavin").quantity
    p_quan = Medicine.objects.get(name="Pyridoxine").quantity
    c1_quan = Medicine.objects.get(name="Cobalamin").quantity
    a_quan = Medicine.objects.get(name="Ascorbate").quantity
    c2_quan = Medicine.objects.get(name="Cholecalciferol").quantity

    context = {
         'r_quan': r_quan,
         'p_quan': p_quan,
         'c1_quan': c1_quan,
         'a_quan': a_quan,
         'c2_quan': c2_quan,
        }


    return render(request,'main/supplies.html',context)

def tables_ins(request):
    context = {
          'officers': Officer.objects.all()
    }

    return render(request,'main/tables_ins.html',context)

def tables_pat(request):
    context = {
          'patients': Patient.objects.all()
    }

    return render(request,'main/tables_pat.html',context)

def success_ins(request):
    return render(request,'main/success_ins.html')

def success_pat(request):
    return render(request, 'main/success_pat.html')

def contact(request):
    return render(request, 'main/contact.html')

def management(request):
    return render(request, 'main/management.html')
