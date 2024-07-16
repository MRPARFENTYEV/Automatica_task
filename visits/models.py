import datetime

from django.db import models


class Worker(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    def search_by_name(self, name):
        return self.filter(full_name__icontains=name)
    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

class Store(models.Model):
    title = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

class Visit(models.Model):
    data_time =  models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(Worker, blank=False, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, blank=False, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.data_time} {self.worker} {self.store} {self.latitude} {self.longitude}'
    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"




# Create your models here.
