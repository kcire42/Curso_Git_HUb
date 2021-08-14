'''
Esto es un ejemplo
'''

class Ingresar_datos:


    def enteros(texto):
        while True:
            try:
                numero = int(input(texto+": "))
                return numero
                break
           
            except ValueError:
                print("Error solo acepto numero enteros")


    def decimales(texto):
        while True:
            try:
                numero = float(input(texto+": "))
                return numero
                break
            except ValueError:
                print("Error solo acepto decimales")


    def cadenas(texto):
        cadena = str(input(texto+": "))
        return cadena
    
            
            
        
    






if __name__ == '__main__':
 numero = Ingresar_datos.enteros("Ingrese numero entero por fa")
 print (numero)
 numero_2 = Ingresar_datos.decimales("Ingrese un deci")
 print (numero_2)
 cadena = Ingresar_datos.cadenas("Ingrese su nombre")
 print(cadena)