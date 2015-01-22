from django.contrib import admin
from models import  Cliente, Profissional
from django.contrib.admin.options import ModelAdmin

# Register your models here.

class AdminProfessional(ModelAdmin):
	list_display = ('nome','email','rua','bairro','numero','senha','foto','area_de_atuacao','criado_em',)
	search_fields = ('nome','area_de_atuacao')
	list_filter = ('nome','rua','bairro','area_de_atuacao')

class AdminClient(ModelAdmin):
	list_display = ('nome','email','rua','bairro','numero','senha','foto',)
	search_fields = ('nome',)

admin.site.register(Cliente,AdminClient)
admin.site.register(Profissional, AdminProfessional)
