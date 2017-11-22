from django.shortcuts import render
from django.contrib.auth.models import User
from textnowapp.models import *
from PIL import Image
from django.views.decorators.csrf import csrf_exempt



def register(request):
	"""
	Aca se le asignará las views para la página de registrarse. Con los datos que nos brinda los inputs
	en el GET de la URL, podremos rellenar los datos del objeto User y crear un usuario nuevo. Tambien 
	verificar si existe o no.
	input: Request hecha por el archivo de urls para el url de register
	output: El render de la plantilla que tendremos para la url determinada
	"""
	
	usu=""
	contra=""
	get=False
	
	
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
	usersList=User.objects.all()
	return render(request,'chat/home.html',{'usersList':usersList,})

def chat(request,u1,u2):
	"""
	Funcion que maneja el chat y los mensajes del chat, aca crearemos un nuevo chat en nuestra tabla
	de chats. A estos chats le asignaremos los mensajes del chat, y el usuario que lo mando. 
	Input: Aqui tendremos el input del request de la Url, el id del usuario1 y el id del usuario2.
	Output: Crearemos el chat asignado a los dos usuarios, y crearemos una lista con los mensajes que
	tendremos en el GET del url.
	"""
	chat= None
	user1 = User.objects.get(pk=u1)
	user2 = User.objects.get(pk=u2)
	


	chats=Chat.objects.all()
	for c in chats:
		if user1 in c.users.all():
			if user2 in c.users.all():
				chat=c
				
	#Crear un chat
	if chat == None:
		chat= Chat(tittle=user1.username +" y "+ user2.username)
		chat.save()
		chat.users.add(user1)
		chat.users.add(user2)
		chat.save()

	if request.GET:
		id_conv = request.GET['conversacionid']
		conv=Chat.objects.get(pk=id_conv)
		if id_conv:
			men=Msg(group=conv, sender=user1)
			msg = request.GET['Mensaje']
			
			if msg:
				men.message =msg 

			men.save()
						
	mensajes = Msg.objects.filter(group=chat)
	


	return render(request,'chat/chatlog.html',{'chat':chat,'mensajes':mensajes})



# Create your views here.
