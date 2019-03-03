#José Luis Macías Vázquez Grupo 03
#Es un programa en el que ingresas un numero arabigo y regresa un el número romano. Solo del uno al diez.

def numeroRomano(n):
    if n == 1:
        numero = "I"
    elif n == 2:
        numero = "II"
    elif n == 3:
        numero = "III"
    elif n == 4:
        numero = "IV"
    elif n == 5:
        numero = "V"
    elif n == 6:
        numero = "VI"
    elif n == 7:
        numero = "VII"
    elif n == 8:
        numero = "VIII"
    elif n == 9:
        numero = "IX"
    elif n == 10:
        numero = "X"
    else:
        numero = "Error. El número no está dentro del rango aceptado. "
    return numero



def main():

    n = int(input("Escribe el número romano: "))
    numero = numeroRomano(n)
    print ("El número en romano es: " , numero)

main()

