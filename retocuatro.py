#1.- Ahora todos los valores que representan a un usuario: Nombre, apellidos, número de teléfono y correo electrónico deberán almacenarse en un diccionario.

#2.- Se añadirá la opción de poder listar el ID de todos los usuarios registrados hasta el momento.

#3.- Se añadirá la opción de poder ver la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este conocer la información registrada.

#4.- Se añadirá la opción de poder editar la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este el programa pedirá nuevamente los valores de un registro para actualizarlos.

#Estas 3 nuevas opciones deberán ser presentadas al usuario al comienzo del programa, esto con la finalidad que sea el usuario quien defina que quiere hacer justo ahora: añadir nuevos usuario, consultarlos o editarlos.

#Un Tip. Para estas nuevas opciones puedes presentarle a tu usuario un pequeño menú del cual pueda elegir. Por ejemplo opción A.-) registrar nuevos usuarios, opción B.-) listar usuarios, Opción C.-) Editar usuarios y así sucesivamente.


#De igual forma el programa tendrán una quinta opción que le permita la usuario finalizar el programa cuando él lo desee.


#Menú: añadir usuario, listar usuarios, consultar usuario, editar usuario,
sistem_options = ""
registers = []
registers_search = {}

while sistem_options != "5":

    print("Bienvenido al sistema, escoge que quieres hacer: ")
    print("1. Añadir usuario")
    print("2. Listar usuarios")
    print("3. Consultar usuario")
    print("4. Editar usuario")
    print("5. Salir")


    sistem_options = str(input('Ingresa el número con la acción que quieres realizar: '))


    match sistem_options:
        case '1': # Registrar un usuario en el sistema

            amount_data = int(input('Ingrese la cantidad de registros que desea realizar: ') )

            minimun_length, max_length, phone_length = 5, 50, 10 
            

            for index, data in enumerate(range(0, amount_data)  ):
                register_dictionary = {} 

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
                register_dictionary['ID']  = len(registers)+1
                register_dictionary['username']     = username
                register_dictionary['lastname']     = lastname
                register_dictionary['phone_number'] = phone_number
                register_dictionary['email']        = email
                registers.append(register_dictionary)
                
            #persons = list(register_dictionary.values())
            #persons = [index+1, username, lastname, phone_number, email]
            
            print('Se han realizado ' + str(amount_data) + ' registros.')
        
        case '2':# Consultar los IDS de los usuarios en el sistema
           
            print('Los ids registrados son: ')
            for index, register in enumerate(registers):
                print('ID',register['ID'])
                print('nombre',register['username'])

            #for register in registers:
             #   print('Los datos del usuario', register['index'])
                
        case '3': #Consultar la información de un usuario

            searchUser = str( input('Por favor ingresa el ID a consultar: ') )
            
            # Buscar la información del usuario
            for index, register in enumerate(registers, start=1):
                key = f"id{index}"
                registers_search[key] = register

            print('Esta es la información del usuario')

            # Si el usuario se encuentra mostrar la información de lo contrario no existe.
            information = registers_search.get('id'+searchUser)
            if information:
                 # Imprimir la informationrmación del diccionario con 'ID' : 1
                print('ID',information['ID']) 
                print('Nombre',information['username']) 
                print('Apellidos',information['lastname']) 
                print('Telefóno',information['phone_number']) 
                print('Telefóno',information['email'])

            else:
                print('El valor no existe en el sistema')
        
        case '4':
            searchUser = str( input('Por favor ingresa el ID a editar: ') )
            
            # Buscar la información del usuario
            for index, register in enumerate(registers, start=1):
                key = f"id{index}"
                registers_search[key] = register

            print('Esta es la información del usuario')
            
            # Si el usuario se encuentra mostrar la información de lo contrario no existe.
            information = registers_search.get('id'+searchUser)
            if information:
                 # Imprimir la información del diccionario con ID que quizo buscar
                print('ID',information['ID']) 
                print('Nombre',information['username']) 
                print('Apellidos',information['lastname']) 
                print('Telefóno',information['phone_number']) 
                print('Telefóno',information['email'])

                print('Agrega la nueva información del usuario: ')
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
                
                information['username']     = username
                information['lastname']     = lastname
                information['phone_number'] = phone_number
                information['email']        = email

            else:
                print('El valor no existe en el sistema')
            
            
print("Gracias por usar el menú.")



