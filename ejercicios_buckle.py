def ejercicio_1():
    nombre = str(input("Ingrese su nombre:"))
    repeticiones = int(input("Ingrese el numero de veces que desea repetirlo:"))
    for i in range (repeticiones):
        j = i + 1
        print (f" {j}- {nombre}")


def ejercicio_2():
    print("hola")


def ejercicio_3():
    pass


if __name__ == "__main__":
    opcion = int(input("Ingrese el programa que desea ejecutar:"))
    print("""
    1- Ejercicio 1 
    2- Ejercicio 2 
    3- Ejercicio 3
    """)
    if opcion == 1:
        ejercicio_1()
    elif opcion == 2:
        ejercicio_2()
    elif opcion == 3:
        ejercicio_3()

           