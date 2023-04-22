#Diccionario que imprima notas del estudiante
sampleDict = {
"class": {
"student": {
"name": "Mike",
"marks": {
"physics": 70,
"history": 80,
"math": 90
},
}
}
}
# print(sampleDict["class"]["student"]["name"])
# print(sampleDict["class"]["student"]["marks"]["physics"])

promedio_final = (sampleDict["class"]["student"]["marks"]["physics"] + sampleDict["class"]["student"]["marks"]["history"]+sampleDict["class"]["student"]["marks"]["math"])/3
# print(promedio)
newDict = {

    "nombre" : sampleDict["class"]["student"]["name"],
    "promedio" : promedio_final
}
print("El resultado es : ")
print(newDict)