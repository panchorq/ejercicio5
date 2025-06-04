palabras = []
vocales = []
no_vocales = []
while True:
    palabra = input("Ingrese una palabra (SALIR para finalizar): ")
    if palabra == "SALIR":
        break
    palabras.append(palabra)


for i in palabras:
    if i[0].lower() in "aeiou":
        vocales.append(i)
    else:
        no_vocales.append(i)

print(f"Las vocales son: {vocales}")
print(f"Las consonantes son: {no_vocales}")
        