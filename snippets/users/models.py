from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class User(models.Model):
	slug = AutoSlugField(populate_from='username', always_update=False)
	pass

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse('user_detail', args=[str(self.slug)])
