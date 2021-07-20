def longitud_cadena():
    cadena = input(str("Ingrse la cadena"))
    j = 0
    for i in cadena:
        j += 1
    print(j)


def pares_impar():
    numero = float(input("Ingrese el numero que desee si es impar o no "))
    modulo = numero % 2
    if modulo == 0:
        print("El numero es par")
    if modulo == 1:
        print("El numero es impar")
    

def generador_contraseñas():
    letras_minusculas = ("a","b","c","d","f","g","h","i","j","k","l","m","")


if __name__ == "__main__":
    opcion = int(input("Ingrese el numero deseado"))
    print("""
    1- Longitud de Cadena
    2- Numero  par y impar
    3- Generador de contraseñas
    """)

    if opcion == 1:
        longitud_cadena()
    if opcion == 2:
        pares_impar()