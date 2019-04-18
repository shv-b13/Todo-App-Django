from django.db import models
from datetime import datetime
# Create your models here.
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class Mood(models.Model):
	status = models.CharField(max_length=500)
	exercise = models.BooleanField(default=False)
	scale = models.IntegerField(
		choices = PRODUCT_QUANTITY_CHOICES,
		default = PRODUCT_QUANTITY_CHOICES[0],
		)
	data = models.DateField(blank=True, null=True)


	def publish(self):
		self.data = datetime.now()
		self.save()

	def __str__(self):
		return self.status