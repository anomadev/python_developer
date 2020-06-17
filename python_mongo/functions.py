import os
import pprint

def clear_system(function):
	def wrap(*args, **kwargs):
		os.system('clear')
		result = function(*args, **kwargs)
		input('')
		os.system('clear')


	wrap.__doc__ = function.__doc__
	return wrap

def show_user(user):
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(user)

@clear_system
def create_user(collection):
	"""a) crear un usuario"""
	username = input('Username: ')
	edad = int(input('Edad: '))
	email = input('Email: ')

	user = dict(username=username, edad=edad, email=email)

	direccion = input('¿Desea ingresar su dirección? (S/N)').lower()
	if direccion == 's':
		user['direccion'] = get_address()

	collection.insert_one(user)
	show_user(user)
	return user

def get_address():
	calle = input('Calle: ')
	ciudad = input('Ciudad: ')
	estado = input('Estado: ')
	codigo_postal = input('Codigo Postal: ')

	direccion = dict(calle=calle, ciudad=ciudad, estado=estado, codigo_postal=codigo_postal)
	return direccion

@clear_system
def get_user(collection):
	"""b) consultar usuario"""
	username = input('Username: ')
	user = collection.find_one(
		{'username': username},
		{'_id': False}
	)

	if user:
		show_user(user)
		return user
	else:
		print('No se encontro documento con el username indicado')

@clear_system
def delete_user(collection):
	"""c) eliminar usuario"""
	username = input('Username: ')
	return collection.remove({'username': username})

def update_user():
	"""d) actualizar usuario"""
	print('Actualizar usuario')

def default(*args, **kwargs):
	print('Opción no valida')