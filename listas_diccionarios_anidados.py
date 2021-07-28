

def main():
    lista = [1,"hola",4.5]
    diccionario = {"Nombre":"Nayeli", "Apellido":"Crisantos", "Ocupacion":"Doctora"}
    super_list = [
        {"Nombre":"Nayeli", "Apellido":"Crisantos", "Ocupacion":"Doctora"},
        {"Nombre":"Erick", "Apellido":"Carrillo", "Ocupacion":"Ingeniero"},
        {"Nombre":"Jose", "Apellido":"Bautista", "Ocupacion":"Abogado"}
    ]
    super_dict = {
        "Primos":[1,3,5,7],
        "Pares":[2,4,6,8],
        "Decimales":[1.0,2.1,3.1,4.1]
    }

    for key,value in super_dict.items():
        print(key, "-",value)
    for i in super_list:
        print(i)
    for diccionario in super_list:
        for key, value in diccionario.items():
            print(key,"-",value)


if __name__ == "__main__":
    main()