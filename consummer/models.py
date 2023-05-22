from django.db import models

# Create your models here.
class Image_upload(models.Model):
    image_name=models.CharField(max_length=150)
    image=models.ImageField(upload_to="Demo/")
    class Meta:
        db_table="Image"