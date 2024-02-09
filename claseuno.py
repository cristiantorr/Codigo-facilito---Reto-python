#variables 

first_name = "cristian torres";
last_name = "torres patiño";
full_name = first_name + "" + last_name;
print(first_name);

age    = 34;
score  = 7.8;
active = True;
print(age, score, active);

#tipos de datos
result = type(active);
print(result);

#Pedir datos por consola ejmplo 1
""" 
data =  input("Ingresa tu nombre");
print("Se ingreso por teclado: " + data); """

#Pedir datos por consola ejmplo 2
# Funciones int y float para poder sobreescribir las variables de tipo string
name    = input('Ingresa tu nombre: ');
age     = int(input('Ingresa tu edad: '));
score   = float(input('Ingresa tu calificación: '));
# Operadores relacionales ( ==, !=, >, >=, <, <=) retornan boolean
active  = input('El usuario se encuentra activo? (si/no)') == 'si'

age = int(age);
print(name, age, score, active);

# Funciones print - input - int - float - str 
print( type( str(10) ) ) #convierte a string

