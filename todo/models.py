from django.db import models

# Create your models here.
class Todo(models.Model):
	CHOICES_STATUS_LIST = (
		('active', 'active'),
		('done', 'done'),
		('cancled', 'cancled'))
	text = models.TextField()		
	status = models.CharField(
		max_length = 7,
		choices = CHOICES_STATUS_LIST,
		default ='active')

	def __str__(self):
		return self.text