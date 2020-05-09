from django.db import models
from .cars import car_list, body_list, eng_list, drive_list, model_list, reg_list

# Create your models here.
class Price(models.Model):

    car = models.IntegerField(default=0, choices=car_list)
    body = models.IntegerField(default=0, choices=body_list)
    mileage = models.IntegerField(default=0)
    engV = models.IntegerField(default=0)
    engType = models.IntegerField(default=0, choices=eng_list)
    registration = models.IntegerField(default=0, choices=reg_list)
    year = models.IntegerField(default=0)
    model = models.IntegerField(default=0, choices=model_list)
    drive = models.IntegerField(default=0, choices=drive_list)
    