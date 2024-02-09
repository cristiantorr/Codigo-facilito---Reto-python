#Tuplas y Diccionarios: Son estructuras de datos
# Tuplas a diferencia de las listas no pueden modificar su longitud es inmutable, no se pueden añadir ni quitar datos.
# las alistas son mutables y pueden agregar o no datos para modificar su longitud.

# A comparación de las listas, las tuplas se hacen con parentesis
settings = ('localhost', 3006, 'root', 'password', 'database')
print(settings)

#Se le indica a python que tengo 5 variables son igual a las de settings
host, port, username, password, database = settings
# también se pueden acceder a varias variables sin tener que imprimir las demás ejemplo: *_
host, _, root, *_ = settings
print(host, root)

# Podemos anidar tuples

tuples = (
  (1, 2, 3),
  (4, 5, 6),
  (7, 8, 9)
)

#Para evitar palabras reservadas e indicarle al lenguaje que no utilizamos dicha palabra como en este caso tuple, le ponemos guión bajo _tuple
for _tuple in tuples: 
    print(_tuple)

# Podemos imprimir las tuples de otra forma si ya sabemos cuántos elementos hay en tuples.
    
for number1, number2, number3 in tuples:
    print(number1, number2, number3)

#DICCIONARIOS - Los diccionarios también son estructuras de datos para almacenar diferentes tipos de datos.
# La diferencia entre diccionario y tuplas es que los diccionarios no trabajan con indices, trabajan con llaves, clave, valor
    
# Las llaves no son strings son Objetos inmutables (String, Enteros, Flotantes, Bool, Tuplas)
    
#Metódos keys, valies, items
    
user = {
    'name'   : 'Cody',
    'age'    : 10,
    'email'  : 'ps4cristiantorr@gmail.com', 
    'active' : True,
    10 : 3.14,
    True: 'Verdadero',
    (1, 2, 3) :'Tupla'
}

print(user)
#Validar si el valor esta ene l diccionario para evitar errores
if 'name' in user:
    print( user['name'])

#Otra forma de validar si existe un valor es con el método get(valor, mensaje optional)
value = user.get('username', 'No existe la llave') # Retorna None -> nada (representa nada, niun valor)
print(value)

#Metódo keys : Podemos ver todas nuestras llaves
print( user.keys() )

#Metódo values : Podemos ver todos nuestros valores
print( user.values() )
print( tuple( user.values() ) ) #Podemos convertirlo en tuple
print( list( user.values() ) ) #Podemos convertirlo en lista

#Metódo items: Retorna tuplas 
#print( user.items() )




