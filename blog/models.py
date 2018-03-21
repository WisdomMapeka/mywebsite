from django.db import models


class Post(models.Model):
	name = models.CharField(max_length = 300)
	DOB = models.DateField()
	known = models.TextField()
	lives = models.TextField()

	def __str__(self):
		return self.name

class Quotes(models.Model):
	quote = models.ForeignKey(Post, on_delete=models.CASCADE)
	quotes = models.TextField()
	name = models.CharField(blank=True, default='', max_length=200)

	def __str__(self):
		return self.quotes[:7]
		
