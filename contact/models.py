from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class Contact(models.Model):
    ismingiz = models.CharField(max_length=150)
    familiyangiz = models.CharField(max_length=150)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon raqamni quyidagi ko'rinishda kiritishingiz kerak: '+999999999'. 15 tagacha belgi kiritishingiz mumkin.")
    telefon = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField()
    xabar = models.TextField()

    def __str__(self):
        return self.xabar

    def get_absolute_url(self):
        return reverse('xabarlar')