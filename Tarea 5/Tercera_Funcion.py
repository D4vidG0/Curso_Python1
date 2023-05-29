#Este es el ejercicio 3 de la Tarea 2
#papa + roto = praoptao

string1 = input ("Escriba la primera palabara : ")
string2 = input ("Escriba la segunda palabra : ")

print(f"La primera palabra es: \n{string1}")
print(f"La segunda palabra es: \n{string2}")

#Limpieza de datos

input_min1 = string1.lower() #conviertiendo todo a minusculas
input_min2 = string2.lower()
input_min1 = input_min1.replace(" ", "") #quitando espacios
input_min2 = input_min2.replace(" ", "")

a = len(input_min1)
b = len(input_min2)
i=0
#Aca era la funcion original para intercalar. 
# if a == b: 
#     print("La dos palabras intercalada son:")

#     while i < a:
#         palabra = input_min1[i]+input_min2[i]
#         palabra = palabra.replace(" ", "") #eliminar espacios
#         print(palabra , end="")
#         i+=1

# else:
#     print("ERROR: Palabras no son del mismo tamano")
#Aca empieza la parte nueva
if a == b: 
       test = list(map(lambda str1,str2: str1+str2, string1,string2)) # Aca se utiliza la lambda y map para juntar los strings y los devuelve en una lista
       print("La palabra combinada es:")
       print((" ".join(test)).replace(" ", "")) #se utiliza join para unir las palabras y replace para quitar espacios. 
else:
     print("ERROR: Palabras no son del mismo tamano")