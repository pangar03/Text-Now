from django.shortcuts import render
from django.contrib.auth.models import User


def register(request):
	"""
	Aca se le asignará las views para la páginade registrarse  
	input: Request hecha por el archivo de urls para el url de register
	output: El render de la plantilla que tendremos para la url determinada
	"""
	get=False
	usu=""
	contra=""
	
	if request.GET:
		if request.GET['Usuario'] and request.GET['Contraseña']: 
			usu=request.GET['Usuario']
			contra = request.GET['Contraseña']
			if User.objects.filter(username=usu).exists():
				usuarioex=True
			else:
				newuser= User.objects.create_user(usu,'',contra)
				get=True
				usuarioex=False

	return render(request,'auth/register.html',{'Usuario':usu, 'Contrasena':contra, 'geto':get})

def home(request):
	"""
	Funcion que manda a la pantalla de home despues de haber logeado correctamente a la plataforma.
	Input: Request hecha por el LOGIN_REDIRECT_URL dentro del archivo settings.py
	Output: Render de la pagina Home
	"""
	return render(request,'chat/home.html',{})


# Create your views here.
