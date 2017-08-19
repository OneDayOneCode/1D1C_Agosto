
def convertir_romano(numero_decimal):
    numeros_romanos = [
            "I", "II", "III",
            "IV", "V", "IV",
            "IIV", "IIV", "IIIV",
            "X"
            ]

    if(numero_decimal != 0):
        print(f"{numeros_romanos[numero_decimal-1]}")
    else:
        print("El numero no esta en un rango del 1 al 10")

try:
    convertir_romano(int(input("Numero:")))
except IndexError:
    print("El numero no esta en un rango el 1 al 10")
except ValueError:
    print("El numero no es un dato numerico entero")
