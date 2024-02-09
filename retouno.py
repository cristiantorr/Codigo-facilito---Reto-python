# Reto 1: Ingresar un usuario al sistema 
# Datos: Nombres, apellidos, no.telefono, correo electrónico
# Mensaje bienvenida: Hola + nombreCompletoUsuario + correoElectronico


print("Bienvenido al sistema, por favor ingresa tus datos")

username     = input('Ingresa tus Nombres: ')
lastname     = input('Ingresa tus Apellidos: ')
phone_number = input('Ingresa tu Número de teléfono: ')
email        = input('Ingresa tu Correo electrónico: ')
#print(type(username), type(lastname), type(phone_number), type(email) )

print("Hola, " + username + ' ' + lastname + ' <' + email + '>' )