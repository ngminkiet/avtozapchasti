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

    spare_parts_types = (
        ('bodywork', 'кузов'),
        ('fasteners', 'крепёж'),
        ('heating_and_ventilation', 'отопление и вентиляция'),
        ('steering_control', 'рулевое управление'),
        ('engine', 'двигатель'),
        ('salon', 'салон'),
        ('cooling_system', 'система охлождения'),
        ('fuel_system', 'топливная система'),
        ('brake_system', 'тормозная система'),
        ('transmission', 'трансмиссия'),
        ('filters', 'фильтры'),
        ('undercarriag', 'ходовая часть'),
        ('electrics', 'электрика'),
        ('summer_tires', 'летние шины'),
        ('winter_tires', 'зимние шины'),
        ('alloy_discs', 'литые диски'),
        ('tamped_discs', 'штампованные диски'),
        ('forged_discs', 'кованые диски'),
        ('passenger_car_batteries', 'легковые аккумуляторы'),
        ('cargo_batteries', 'грузовые аккумуляторы'),
        ('bike_batteries', 'мотоаккумуляторы'),
        ('cigarette_lighter_wires', 'провода прикуривания'),
        ('engine_oils', 'моторные масла'),
        ('brake_fluid', 'тормозная жидкость'),
        ('antifreeze', 'антифриз'),
        ('transmission_oil', 'трансмиссионная масло'),
        ('distilled_water', 'дистиллированная вода')
    )

    item_title = models.CharField(max_length=50) # заголовок товары
    price = models.IntegerField() # цена
    description = models.TextField() # описание
    photo = models.ImageField() # фото товара
    material = models.CharField(max_length=20) # материал
    spare_parts_type = models.CharField(max_length=25, choices=spare_parts_types)# тип запчасти
    spare_parts_color = models.CharField(max_length=20)# цвет запчасти


    def __str__(self):
        return f'{self.id}. {self.item_title}'
