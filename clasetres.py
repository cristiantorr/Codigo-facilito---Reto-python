# Listas = Estructuras de datos

my_list = [1, 3.14, 'string', True, [2, 3.111, "Example", False]]
#print(my_list)

#Indices de izquierda a derecha en una lista
#0 -> python 
#1 -> Django 
#2 -> Flask 
#3 -> Ruby 
#4 -> Ruby on Rails 
#5 -> Rust 
# 6 -> C#

#Indices de derecha a izquierda en una lista, se puede colocar -2 = Rust
# -7 python 
# -6 Django 
# -5 Flask 
# -4 -> Ruby 
# -3 -> Ruby on Rails 
# -2 -> Rust 
# - 1 -> C#
courses =  ['Python', 'Django', 'Flask', 'Ruby', 'Ruby on Rails', 'Rust', 'C#'] # El total de elementos - 1 = Al último elemento

last_index = len(courses) - 1
#print(courses[last_index])

#index = int( input('Ingresa el indice para conocer su valor:') )
#print(courses[index])

#Validar si el indice es balido
""" if index <= last_index:
    print(courses[index])
else:
    print('Lo sentimos, el índice NO es válido.') """

#sublista de la lista courses
new_list = courses[0:5] # El indice 5 no se toma en cuenta ya que empieza desde el 0 al 4
print(new_list)
new_list3 = courses[3:] # Desde el indice 3 al último
print(new_list3)
new_list5 = courses[:5] # El indice 5 no se toma en cuenta ya que empieza desde el 0 al 4
print(new_list5)
new_listCopia = courses[:] # Hará una copia desde el indice 0 al último indice
print(new_listCopia)
new_listSaltos = courses[::2] # Hace saltos de 2 en 2 en la lista, se cambia el valor por cualquier salto
print(new_listSaltos)
new_listInverso = courses[::-1] # Genera la lista al inverso
print(new_listInverso)

#Reemplazar un valor de la lista
courses[0] = 'CódigoFacilito'
print(courses)



