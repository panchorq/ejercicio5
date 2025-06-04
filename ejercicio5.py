numeros = []
while True:
    num = input("Ingrese un numero (0 para salir): ")
    try:
        num = int(num)
        if num == 0:
            break
    except ValueError:
        print("Ingrese los datos correctamente")
    numeros.append(num)
    
numeros.sort()
print(f"El numero menor es {numeros[0]} y el mayor es {numeros[-1]}")

    