from collections.abc import Iterable
from django.db import models
from django.core.files import File
from django.conf import settings

from main.models_dir import m02_users
import cv2
import os


class Property(models.Model):

    name                    = models.CharField(max_length = 120, blank = True, null = True)
    price                   = models.IntegerField(blank = True, null = True)
    cur                     = models.CharField(max_length = 4, blank = True, null = True)

    upload_date             = models.DateField(blank = True, null = True)

    details                 = models.TextField(max_length = 1024, blank = True, null = True)

    number_of_rooms         = models.IntegerField(blank = True, null = True)
    number_of_bathroom      = models.IntegerField(blank = True, null = True)
    category                = models.CharField(max_length = 120, blank = True, null = True)
    property_type           = models.CharField(max_length = 120, blank = True, null = True)
    floor_space             = models.CharField(max_length = 32, blank = True, null = True)
    land_area               = models.CharField(max_length = 32, blank = True, null = True)
    condition               = models.CharField(max_length = 120, blank = True, null = True)
    year_of_construction    = models.CharField(max_length = 25, blank = True, null = True)
    building_levels         = models.IntegerField(blank = True, null = True)
    elevator                = models.BooleanField(blank = True, default = False)
    heating                 = models.CharField(max_length = 120, blank = True, null = True)
    views                   = models.CharField(max_length = 120, blank = True, null = True)
    orientation             = models.CharField(max_length = 120, blank = True, null = True)
    interior_height         = models.CharField(max_length = 120, blank = True, null = True)
    air_condition           = models.BooleanField(blank = True, default = False)
    attic                   = models.CharField(max_length = 120, blank = True, null = True)
    parking                 = models.CharField(max_length = 120, blank = True, null = True)
    balcony                 = models.BooleanField(blank = True, default = False)
    bathroom_toilet         = models.CharField(max_length = 120, blank = True, null = True)
    images_videos           = models.ManyToManyField("PropertyImagesVideos", blank = True)
    extra_features          = models.TextField(blank = True, null = True)

    country                 = models.CharField(max_length = 256, blank = True, null = True)
    city                    = models.CharField(max_length = 256, blank = True, null = True)
    address                 = models.CharField(max_length = 1024, blank = True, null = True)
    lat                     = models.FloatField(blank = True, null = True)
    lon                     = models.FloatField(blank = True, null = True)

    document                = models.FileField(blank = True, null = True)
    approved                = models.BooleanField(blank = True, default = False)

    lister                  = models.ForeignKey(m02_users.CustomUser, on_delete = models.CASCADE, blank = True, null = True)
    
    def __str__(self):
        return self.name





class PropertyImagesVideos(models.Model):
    file                    = models.FileField(upload_to = "images_videos", blank = True, null = True)
    file_type               = models.CharField(max_length = 32, blank = True, null = True)
    
    # Thumbnail only for video
    thumbnail               = models.FileField(upload_to = "images_videos", blank = True, null = True)

    def save(self, *arg, **kwarg):
        
        vcap = cv2.VideoCapture(self.file.path)
        res, im_ar = vcap.read()
        base_dir = settings.BASE_DIR

        filename = self.file.name.split("/")[1]
        cv2.imwrite(f"{base_dir}/media/temp/{filename}.png", im_ar)
        file = f"{base_dir}/media/temp/{filename}.png"

        with open(file, "rb") as f:
            django_file = File(f)
            self.thumbnail.save(os.path.basename(file), django_file, save=False)

        return super().save(arg, kwarg)

    def __str__(self) -> str:
        return f"{self.file_type}_{self.id}"