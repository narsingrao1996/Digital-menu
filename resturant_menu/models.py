from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("main_dishes", "Main Dishes"),
    ("fast_food", "Fast Food"),
    ("desserts", "Desserts")
)

STATUS = (

    (0,"unavailable"),
    (1, "available")
)


class Item(models.Model):
    meal = models.CharField(max_length=1000,unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    meal_type = models.CharField(max_length=200,choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS,default=1)
    dish_images = models.ImageField(upload_to='images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.meal