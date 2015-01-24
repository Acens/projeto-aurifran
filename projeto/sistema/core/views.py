from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request,'index.html',{})

def profissionais(request):
	return render(request, 'profissionais.html',{})

def pacientes(request):
	return render(request, 'paciente.html',{})