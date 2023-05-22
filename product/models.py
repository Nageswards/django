from django.db import models

# Create your models here.
class Food_type(models.Model):
    
    name =models.CharField(max_length=50)
    class Meta:
        db_table="Food_cat"

class Food(models.Model):
    food_name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    food_type = models.ForeignKey("Food_type",on_delete=models.CASCADE,blank=True,null=True)
    item_price = models.IntegerField()
    image_Food = models.ImageField(upload_to="product/")
    class Meta:
        db_table="Image_Food"

