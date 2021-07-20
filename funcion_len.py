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
    letras_minusculas = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    letras_mayusculas = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    caracteres_extraños = ("!","","#","$","%","&","/","(",")","=","?","'","¿","¡")
    caracteres = (letras_minusculas, letras_mayusculas, caracteres_extraños)
    print(caracteres)


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
    if opcion == 3: 
        generador_contraseñas()