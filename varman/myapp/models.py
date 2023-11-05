from django.db import models
from django.contrib import admin
class Football_player (models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    number=models.IntegerField()

class Football_playerAdmin(admin.ModelAdmin):
    list_display=['name','age','height','weight','number']