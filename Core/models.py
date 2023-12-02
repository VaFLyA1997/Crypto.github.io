from django.db import models
from django.contrib.auth.models import User

# class Shop(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     # has_routes = models.BooleanField(default=False)
#     arrival_date = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.name
    
# class Asics(models.Model):
#     manufacturer = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     power = models.CharField(max_length=100)
#     energy = models.CharField(max_length=100)


class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class ASIC(models.Model):
    manufacturer = models.CharField("Производитель", max_length=100)
    name = models.CharField("Название", max_length=100)
    power = models.CharField("Мощность", max_length=100)
    energy = models.CharField("Энергопотребление", max_length=100)

    def __str__(self):
        return self.name

class Accessories(models.Model):
    classification = models.CharField("Классификация", max_length=100)
    name = models.CharField("Название", max_length=100)
    # power = models.CharField("Мощность", max_length=100)
    # energy = models.CharField("Энергопотребление", max_length=100)

    def __str__(self):
        return self.name

class ShopASIC(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    asic = models.ForeignKey(ASIC, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    arrival_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.shop.name} - {self.asic.name}"


class ShopAccessories(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.shop.name} - {self.accessories.name}"



class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # has_routes = models.BooleanField(default=False)
    arrival_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    

