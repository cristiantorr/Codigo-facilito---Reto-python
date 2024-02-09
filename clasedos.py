

#Bool
# True / False
# Operadores relacionales ( ==, !=, >, >=, <, <=) retornan boolean
# Operadores lógicos ( and, or,not )
# 
numberone = 10
numbertwo = 20

#and : Todas las comparaciones tienen que ser verdaderas para que sea True
              #TRUE                   #TRUE
resultone = numberone < numbertwo and 10 == 10 #= True
print(resultone)

#or : Basta con que solo una comparación sea verdadera para que todo sea True
resulttwo = numberone > numbertwo or 10 == 10 #= True
print(resulttwo)

#not : Negamos el inverso del booleano ejemplo True el inverso es False y False el inverso es True
resultthree = numberone > numbertwo or 10 == 10 #= True

#Negamos el resultado True con not es False y si volvemos a negar con not el resultado es True
print(not not resultthree)

# Ejemplo con paréntesis 
                #True     #True
resultfour = True and ( True or False )
print(resultfour) # True

                #True     #False
resultfive = True and ( True and False )
print(resultfive) # False

            #True     #True #negación->#True #False  #True
resultsix = True and ( True and ( not (False and (True or False) )))
print(resultsix) # True

