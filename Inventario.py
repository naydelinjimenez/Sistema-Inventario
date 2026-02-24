def cargar_inventario():
    try:
        with open("inventario.txt", "r") as archivo:
            print("\nInventario:\n")
            for linea in archivo:
                datos = linea.strip().split(",")
                print("ID:", datos[0])
                print("Nombre:", datos[1])
                print("Precio:", datos[2])
                print("Cantidad:", datos[3])
                print("-------------------")

    except FileNotFoundError:
        open("inventario.txt", "w").close()


def agregar_producto():
    id = input("Ingrese ID: ")
    nombre = input("Ingrese nombre: ")
    precio = input("Ingrese precio: ")
    cantidad = input("Ingrese cantidad: ")

    with open("inventario.txt", "a") as archivo:
        archivo.write(id + "," + nombre + "," + precio + "," + cantidad + "\n")

    print("Producto agregado correctamente.\n")


def menu():
    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Ver inventario")
        print("2. Agregar producto")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_inventario()

        elif opcion == "2":
            agregar_producto()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


menu()