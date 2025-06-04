nombre = input("Ingrese su nombre: ")
notas = []
while True:
    nota = input("Ingrese su nota (0 para salir): ")
    try:
        nota = float(nota)
        if nota == 0:
            break
    except ValueError:
        print("Ingrese los datos correctamente")
    notas.append(nota)
    

print(f"las notas de {nombre} son: ", end="")
for i in notas:
    print(i, end=" ")
print("", end="")
print(f"El promedio de es {sum(notas) / len(notas)}")