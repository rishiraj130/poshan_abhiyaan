from django.db import models
from officer.models import Officer
from PIL import Image
from datetime import date
from django.db.models.signals import post_save

# Create your models here.
class Patient(models.Model):
    patient_id            =            models.AutoField(primary_key=True)
    first_name            =            models.CharField(max_length=30)
    last_name             =            models.CharField(max_length=30)
    relation              =            models.CharField(max_length=30)
    date_of_birth         =            models.DateField()
    phone                 =            models.IntegerField()
    aadhaar               =            models.CharField(max_length=30,default="NILL")
    blood_group           =            models.CharField(max_length=30)
    height                =            models.IntegerField()
    weight                =            models.IntegerField()
    category              =            models.CharField(max_length=30)
    registration_history  =            models.CharField(max_length=30)
    status                =            models.BooleanField(default=True)
    p_image               =            models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_reg           =            models.DateField(default=date.today)
    medical_instructor    =            models.ForeignKey(Officer,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_id)

    def save(self):
        super().save()

        img = Image.open(self.p_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.p_image.path)


def change_availability(sender,instance,created,*args,**kwargs):
        no_patients = len(Patient.objects.filter(medical_instructor=instance.medical_instructor,status=True))
        if no_patients == 2:
            officer = Officer.objects.get(officer_id=int(instance.medical_instructor.officer_id))
            officer.aval = False
            officer.save()




post_save.connect(change_availability,sender=Patient)
