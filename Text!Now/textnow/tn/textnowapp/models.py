from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
	tittle = models.CharField(max_length=30)
	users= models.ManyToManyField(User, blank=True)
	def __str__(self):
		return self.tittle
class Msg(models.Model):
	sender = models.ForeignKey(User)
	group = models.ForeignKey(Chat, on_delete=models.CASCADE)
	message= models.TextField(null=True)
	time = models.TimeField( auto_now_add=True, blank=True)
	def __str__(self):
		m="No hay mensaje"
		if (self.message):
			m= self.message
		return str(self.group) + ": "+m


