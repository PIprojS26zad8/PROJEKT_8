from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nazwa produktu")
    is_bought = models.BooleanField(default=False, verbose_name="Kupione")

    def __str__(self):
        return self.name

