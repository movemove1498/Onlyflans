from django.contrib import messages
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def crear_usuario(request, username:str, first_name:str, email:str, password:str, pass_confirm:str):
    if password != pass_confirm:
        messages.warning(request,' Las contraseñas no coinciden')
        return False
    
    if len(password)> 50:
        messages.warning(request,' La contraseña no puede ser mayor a 50 caracteres')
        return False
    
    try:
        user = User.objects.create_user(
        username,
        email,
        password,
        first_name=first_name,
        )
    except IntegrityError:
        messages.warning(request,'El usuario ya existe')
        return False
        
    except Exception:
        messages.warning(request,'Error al crear el usuario')
        return False
    # si llega aqui se creo el usuario
    messages.success(request,'USUARIO CREADO CON EXITO!! Porfavor ingrese')