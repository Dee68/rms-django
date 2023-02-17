from django.db import models
from django.utils.safestring import mark_safe
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.

class Meals(models.Model):
    CATEGORY = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('supper', 'supper')
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, upload_to="meals/")#CloudinaryField('image', overwrite=True, resource_type='image')
    category = models.CharField(max_length=9, choices=CATEGORY, default='lunch')
    slug = models.SlugField(max_length=200)
    number_of_persons = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'meals'
        verbose_name_plural = 'meals'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" height="50" width="50">' %self.image.url)
        return "No image found"
    image_tag.short_description = 'Image'

    def __str__(self):
        return str(self.name)


class Reservation(models.Model):
    Table_TYPE = (
        ('single', 'single'),
        ('double', 'double'),
        ('group', 'group')
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # cost = models.DecimalField(max_digits=10)
    reserv_date = models.DateTimeField()
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)

    def __str__(self):
        return f'${self.customer.username} booked for :${self.meal.name} on ${self.reserv_date}'
