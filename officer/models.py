from django.db import models
from PIL import Image

# Create your models here.
class Officer(models.Model):
    officer_id            =            models.AutoField(primary_key=True)
    first_name            =            models.CharField(max_length=30)
    last_name             =            models.CharField(max_length=30)
    date_of_birth         =            models.DateField()
    phone                 =            models.IntegerField()
    gender                =            models.CharField(max_length=30)
    o_image               =            models.ImageField(default='default.jpg', upload_to='profile_pics')
    aadhaar               =            models.CharField(max_length=30)
    degree                =            models.CharField(max_length=30)
    login_number          =            models.CharField(max_length=30,default="NILL")
    aval                  =            models.BooleanField(default=True)

    def __str__(self):
        return str(self.officer_id)


    def save(self):
        super().save()

        img = Image.open(self.o_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.o_image.path)
