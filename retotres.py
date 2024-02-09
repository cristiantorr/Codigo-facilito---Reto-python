# Siempre que se registre usuario de forma exitosa generamos un identificador único para ese registro, Un ID NÚMERICO AUTOINCREMENTAL
# Todos los datos se almacenaran en un listado que se mostrarán en consola.Esto de tal forma que el usuario pueda conocer y tenga certeza que las operaciones, en efecto, se realizaron de forma exitosa.

print("Bienvenido al sistema")

amount_data = int(input('Ingrese la cantidad de registros que desea realizar: ') )

minimun_length, max_length, phone_length = 5, 50, 10 
registers = []


for index, data in enumerate(range(0, amount_data)  ):

  username = input('Ingresa tus Nombres: ')
  while len(username) < minimun_length:
    print('Por favor, el campo nombre debe ser (min: 5 - max: 50) caracteres.') 
    username = input('Ingresa tus Nombres: ')
  

  lastname = input('Ingresa tus Apellidos: ')
  while len(lastname) < minimun_length:
    print('Por favor, el campo apellidos debe ser (min: 5 - max: 50) caracteres.')
    lastname = input('Ingresa tus Apellidos: ')
    
  phone_number = input('Ingresa tu Número de teléfono: ')
  while len(phone_number) < phone_length  :
    print('Por favor, el campo teléfono debe ser de 10 caracteres.')
    phone_number = input('Ingresa tu Número de teléfono: ')

  email = input('Ingresa tu Correo electrónico: ')
  while len(email) < minimun_length:
    print('Por favor, el campo correo electrónico debe ser (min: 5 - max: 50) caracteres.')
    email = input('Ingresa tu Correo electrónico: ')
  
  persons = [index+1, username, lastname, phone_number, email]
  registers.append(persons)


print('Se han realizado ' + str(amount_data) + ' registros.')
print('a continuación estos son los registros: ')

for index, register in enumerate(registers):
   print('Los datos del usuario', index+1)
   for dataperson in register:
     print(dataperson)
     