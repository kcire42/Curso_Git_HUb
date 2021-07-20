def fc_max(numero_1,numero_2,numero_3):
    if (numero_1 > numero_2 and numero_1 > numero_3):
        print(f"numero 1 es mayor: {numero_1}")
    elif (numero_2 > numero_1 and numero_2 > numero_3):
        print(f"numero 2 es mayor: {numero_2}")
    elif (numero_3 > numero_1 and numero_3 > numero_2):
        print(f"numero 3 es mayor: {numero_3}")
    elif (numero_1 == numero_2 == numero_3):
        print(f"Son iguales el numero 1: {numero_1} , el numero 2: {numero_2} y el numero 3: {numero_3}")






if  __name__ == "__main__":
    numero_1 = float(input("Ingrese el numero 1: "))
    numero_2 = float(input("Ingrese el numero 2:"))
    numero_3 = float(input("Ingrese el numero 3:"))
    fc_max(numero_1,numero_2,numero_3)