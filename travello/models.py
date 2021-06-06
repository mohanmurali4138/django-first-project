from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    # def __init__(self,id,name,img,desc,price):
    #     self.id=id
    #     self.name=name
    #     self.img=img
    #     self.desc=desc
    #     self.price=price
    # id:int
    # name:str
    # img:str
    # desc:str
    # price:int