# Métodos append, extend, insert, remove, clear,  count, index

courses =  ['Python', 'Django', 'Flask', 'Ruby', 'Ruby on Rails', 'Rust', 'C#'] # El total de elementos - 1 = Al último elemento

new_courses = ['Java', 'Docker', 'Unix']

# Agregar cursos a la lista
courses.append('Javascript')
courses.append('Typescript')
courses.append('Swift')

# Agregar cursos a la lista pero indicandole en que posición

courses.insert(1, 'SQLServer') #Cuando se agrega el curso desplaza hacia la derecha al que estaba en ese indice

# Extender nuestra lista con el método extends

courses.extend(new_courses) # Con esto se agregara los nuevos cursos new_courses a la lista de cursos

# Removemos cursos con el método remove
courses.remove('Flask')
courses.remove('Ruby')

# Contar cuántas veces esta el valor en la lista
print( 'Cuántas veces esta Rust: ' + str(courses.count('Rust')) )

# Verificar verdadero o false si esta un elemento en la lista 
print( 'Ruby' in courses)

# Verificar si un indice esta en el listado
print( 'Se encuentra en el indice: ' + str(courses.index('Django')) )

# Limpiar por completo la lista
#courses.clear() # Borrada
#print(len(courses)) # Lista 0

#enumerate -> conocer los valores e indices
for index, course in enumerate(courses):
    print('El valor para el indice', index, 'es', course)
for index in enumerate('Hola mundo'):
    print('El valor para el indice', index, 'es', course)

# String en indices, se pueden hacer sublistas y concatenar
    
message = 'Hola mundo'
new_message = 'P' + message[1:]
print( new_message )

# Imprimir listado
print(courses)