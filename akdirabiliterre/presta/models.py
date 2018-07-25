from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.urls import reverse
from django.contrib.gis.db import models as modes
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)

    def __str__(self):
        return self.name


class Ville(models.Model):
    ville=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)

    def __str__(self):
        return self.ville

    # def get_absolute_url(self):
    #     return reverse('zoom_detail', args=[self.slug])
class Prestataire(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    description=models.TextField()
    logo=models.ImageField(upload_to="presta_logo")
    phone_number = PhoneNumberField()
    site=models.CharField(max_length=250, blank=True, null=True)
    address=models.CharField(max_length=250, blank=True, null=True)
    email=models.EmailField(max_length=250, blank=True, null=True)
    facebook=models.CharField(max_length=250, blank=True, null=True)
    twitter=models.CharField(max_length=250, blank=True, null=True)
    Instagram=models.CharField(max_length=250, blank=True, null=True)
    city=models.ForeignKey(Ville, related_name="presta_ville", on_delete=models.CASCADE)
    country=CountryField()
    latitude=models.DecimalField(max_digits=10, decimal_places=6, blank=True)
    longitude=models.DecimalField(max_digits=10, decimal_places=6, blank=True)
    location=modes.PointField(null=True, blank=True)
    validate=models.BooleanField(default=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('presta_detail',args=[self.slug, self.category,self.city])

    def save(self, *args, **kwargs):
        self.latitude  = self.location.y
        self.longitude = self.location.x
        super(Prestataire, self).save(*args, **kwargs)
