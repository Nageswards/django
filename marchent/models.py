from django.db import models

# Create your models here.
class Goods_type(models.Model):
    
    name =models.CharField(max_length=50)
    class Meta:
        db_table="Goods_cat"

class Goods(models.Model):
    Goods_name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    Goods_type = models.ForeignKey("Goods_type",on_delete=models.CASCADE,blank=True,null=True)
    item_price = models.IntegerField()
    image_Goods = models.ImageField(upload_to="marchent/")
    class Meta:
        db_table="Image_Goods"