contactos = {}
while True:
    nombre = input("Ingrese el nombre (SALIR para finalizar): ")
    if nombre == "SALIR":
        break
    while True:
        telefono = input("Ingrese el telefono: ")
        try:
            telefono = int(telefono)
            break
        except ValueError:
            print("Ingrese los datos correctamente")
    contactos[nombre] = telefono

while True:
    buscar = input("Ingrese el nombre o numero a buscar (SALIR para finalizar): ")
    if buscar == "SALIR":
        break
    try:
        buscar = int(buscar)
        for i in contactos.values():
            if i == buscar:
                for j in contactos.keys():
                    if contactos[j] == i:
                        print(f"El nombre de {buscar} es {j}")
                        break
                break
    except ValueError:
        if buscar in contactos:
            print(f"El telefono de {buscar} es {contactos[buscar]}")
        else:
            print("El contacto no existe")
        