from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


# Create your models here.
class Toy(models.Model):
	name=models.CharField(max_length=50)
	description=models.CharField(max_length=50)

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("toys_detail",kwargs={"pk":self.id})



class Finch(models.Model):
	name=models.CharField(max_length=100)
	breed=models.CharField(max_length=100)
	description=models.TextField(max_length=250)
	age=models.IntegerField()
	#M:M
	toys = models.ManyToManyField(Toy)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Feeding(models.Model):
	date=models.DateField()
	meal=models.CharField(
		max_length=1,
		choices=MEALS,
		default=MEALS[0][0]
		)
	#create FK
	finch=models.ForeignKey(Finch,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.get_meal_display()}on {self.date}'

	class Meta:
		ordering=['-date']

class  Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	fav=models.CharField(max_length=50)
