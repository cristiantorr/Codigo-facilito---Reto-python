# Estructuras de control
# if (elif), match (switch), foreach, while

#if <condition (True/False)>:
 #   pass # Palabra reservada para indicar que el grupo if no va hacer nada
""" if False:
    print('La condición se cumple')
    print('se ejecuta desde que sea true')
else:
    print('Este bloque se ejecuta cuando sea false') """

age = int( input('Ingresa tu edad: ') ) 

if age >= 0 and age <= 110:
    if age >= 18:
        print('Tienes la edad para votar.')
    else:
        print('No tienes la edad para votar.')
else: 
    print('La edad no es valida, intenta de nuevo.')

#elif
    
color = 'red'

if color == 'green':
    print('Puede continuar.')

elif color == 'yellow':
    print('Alto parcial.')

elif color == 'red':
    print('Alto total.')

else:
    print('El color no es valido.')


# switch <3.10 versión python agregaron switch se hace con lapalabra match

colormatch = 'yelslow'

match colormatch:
    case 'red':
        print('Alto total.')

    case 'yellow':
        print('Alto parcial.')
    
    case 'green':
        print('Alto continuar.')
    
    case _: #else
        print('Lo sentimos, el color no es valido.')

# foreach -> Cuando sepamos cuántas interaciones se necesitan.

title = "Estructuras de control" 
print(len(title)) 
for caracter in title:
    print(caracter) 
    
# Se toma hasta el 19
for number in range(1, 20):
    #print(number)   

#Numeros pares
    if number % 2 == 0:
        pass
        #print(number)

# Numeros impares con not -> negación
    if not ( number % 2 == 0):
        print(number)

# while   -> Cuando NO sepamos cuantas iteraciones se necesitan (Condición)

""" while <condition>:
    pass """

number_while = 0
while number_while < 10:
    print(number_while) 
    number_while +=1
else: 
    #Se rompe el ciclo
    print('La condición NO se cumple.')


attends = 0
random_while, number_while, max_attends = 5, 0, 5

while number_while != random_while and attends < max_attends:
    number_while = int( input('Ingresa un número: ') )
    attends += 1

else: 

    if number_while == random_while:
        print('Felicidades encontrastes el número.')
    else:
        print('No encontraste el número.')
    
