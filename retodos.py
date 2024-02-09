# Reto 2: Incrementar el funcionamiento del reto 1
# Registrar una N cantidad de usuarios: Se coloca cuántos registros vamos a realizar, si son 5 registros se tienen que registrar 5 personas.
# Validar: Nombre, apellido, correo electrónico tengan una longitud miníma de 5 caracteres y una longitud máxima de 50
# Número de teléfono de 10 dígitos
# Si se ingresan mal los datos el programa notifica y no deja avanzar hasta que ingrese los datos correctos.

print("Bienvenido al sistema")

amount_data = int(input('Ingrese la cantidad de registros que desea realizar: ') )


minimun_length, max_length, phone_length = 5, 50, 10 

for data in range(0, amount_data):

  username = input('Ingresa tus Nombres: ')
  while len(username) < minimun_length:
    print('Por favor, el campo nombre debe ser (min: 5 - max: 50) caracteres.') 
    username = input('Ingresa tus Nombres: ')
  
  lastname = input('Ingresa tus Apellidos: ')
  while len(lastname) < minimun_length:
    print('Por favor, el campo apellidos debe ser (min: 5 - max: 50) caracteres.')
    lastname = input('Ingresa tus Apellidos: ')

  phone_number = input('Ingresa tu Número de teléfono: ')
  while len(phone_number) < phone_length:
    print('Por favor, el campo teléfono debe ser de 10 caracteres.')
    phone_number = input('Ingresa tu Número de teléfono: ')

  email = input('Ingresa tu Correo electrónico: ')
  while len(email) < minimun_length:
    print('Por favor, el campo correo electrónico debe ser (min: 5 - max: 50) caracteres.')
    email = input('Ingresa tu Correo electrónico: ')

print('Se han realizado ' + str(amount_data) + ' registros.')