from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=100)
	owned = models.BooleanField(default=False)
	tracked = models.BooleanField(default=False)
	def __str__(self):
		return self.name
