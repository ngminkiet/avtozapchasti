import os
from django.db import models
from django.conf import settings

#CharField - текстовое поле
#IntegerField - целочисленное поле
#FloatField - дробное поле
#DateField - поле даты

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "images")

def item_discription_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "item_discription")

class Item(models.Model):
    item_title = models.CharField(max_length=50) # заголовок товары
    price = models.IntegerField() # цена
    description = models.FilePathField(path=item_discription_path) #описание
    material = models.CharField(max_length=20) # материал
    spare_parts_type = models.CharField(max_length=20)# тип запчасти
    spare_parts_color = models.CharField(max_length=20)# цвет запчасти
