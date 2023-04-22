#Ejercicio 3 recibe 2 strings del mismo largo y los intercala
#papa + roto = praoptao

string1 = input ("Escriba la primera oracion o palabara : ")
string2 = input ("Escriba la segunda oracion o palabra : ")

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

if a == b: 
    print("La dos palabras intercalada son:")

    while i < a:
        palabra = input_min1[i]+input_min2[i]
        palabra = palabra.replace(" ", "") #eliminar espacios
        print(palabra , end="")
        i+=1

else:
    print("ERROR: Palabras no son del mismo tamano")