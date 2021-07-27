import random


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
    letras_minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letras_mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    caracteres_extraños = ["!","","#","$","%","&","/","(",")","=","?"]
    caracteres = letras_mayusculas + letras_minusculas + caracteres_extraños
    ##print(caracteres)
    contraseña = []
    for i in range (10):
        contraseña_caracter = random.choice(caracteres)
        contraseña.append(contraseña_caracter)
        ##print(contraseña_caracter)
    ##print(contraseña)
    contraseña = "".join(contraseña)    
    print(f"Tu nueva contraseña: {contraseña}")

def palabra_repetida():
    nombre = str(input("Ingrese una palabra: "))
    cantidad = int(input("Ingrese el numero de veces que desea repetirla: "))
    j= 0
    for i in range (cantidad):
        j += 1
        print(f"{j}- {nombre}")

def edad():
    edad = int(input("Ingrese su edad:"))
    edad= edad+1

    for i in range(edad):
        if i == 1:
            print(f"{i} año")
        elif i > 1:
            print(f"{i} años")

def impares():
    numero = int(input("Ingrese un numero"))
    numero =numero+1
    lista_numeros= []
    for i in range(numero):
        modulo = i%2
        if modulo ==1:
            print(i, end=", ")
            #lista_numeros.append(i)
        else:
            continue
    #print(lista_numeros)


def cuenta_atras():
    numero = int(input("Ingrese el numero a contar: "))

    for i in range(0, numero+1):
        print(numero)
        numero-=1

def interes ():
    inversion = float(input("Ingrese la cantidad a invertir: "))
    años_a_invertir = int(input("Ingrese cuantos años vaz a invertir: "))
    interes = 0.1
    ingreso = inversion
    

    for i in range(años_a_invertir):
        ##print(inversion)
        ganancia = inversion * interes
        inversion = inversion + ganancia
        ##print(inversion)
    intereses = inversion-ingreso
    print(f"tu ganancia total despues {años_a_invertir} años es de {intereses} lo que te un total de: {inversion}")


      
        
    


if __name__ == "__main__":
    print("""
    Este es el menu que hice 
    1- Longitud de Cadena
    2- Numero  par y impar
    3- Generador de contraseñas
    4- Palabra Repetida
    5- Edad
    6- Impares
    7- Cuenta_atras
    8- Interes
    """)
    opcion = int(input("Ingrese el numero deseado: "))


    if opcion == 1:
        longitud_cadena()
    if opcion == 2:
        pares_impar()
    if opcion == 3: 
        generador_contraseñas()
    if opcion == 4: 
        palabra_repetida()
    if opcion == 5:
        edad()
    if opcion == 6:
        impares()
    if opcion == 7:
        cuenta_atras()
    if opcion == 8:
        interes()