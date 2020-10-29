from django.db import models
from django.db.models import Model

class Blog(models.Model):
	title 	= models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	body 	= models.TextField()
	image 	= models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return (self.body[:36] + '...')

	def mod_date(self):
		return self.pub_date.strftime('%b %e %Y')
