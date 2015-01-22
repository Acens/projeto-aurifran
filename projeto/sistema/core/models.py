from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Cliente(models.Model):
	class Meta:
		ordering = ('nome','criado_em')

	nome = models.CharField(max_length = 100)
	email = models.EmailField()
	rua = models.CharField(max_length = 100)
	bairro = models.CharField(max_length = 100)
	numero = models.IntegerField()
	senha = models.CharField(max_length = 100)
	foto = models.ImageField(upload_to = 'upload_files/profile_images',default = 'upload_files/profile_images')
	criado_em = models.DateTimeField(default=datetime.now(),blank=True)

	def __unicode__(self):
		return self.nome

	

class Profissional(models.Model):
	
	class Meta:
		ordering = ('nome','criado_em')

	nome = models.CharField(max_length = 100)
	email = models.EmailField()
	rua = models.CharField(max_length = 100)
	bairro = models.CharField(max_length = 100)
	numero = models.IntegerField()
	senha = models.CharField(max_length = 100)
	foto = models.ImageField(upload_to = 'upload_files/profile_images',default = 'upload_files/profile_images')
	area_de_atuacao = models.CharField(max_length = 50)
	criado_em= models.DateTimeField(default=datetime.now(),blank=True)
	curriculo = models.FileField(upload_to = 'upload_files/resumes',default = 'upload_files/profile_images')
	
	def __unicode__(self):
		return self.nome




	







	

