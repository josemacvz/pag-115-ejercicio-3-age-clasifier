#José Luis Macías Grupo 03
#Es un programa que convierte kilometros a millas

def convertirKilometros(k):
    millas = k * .6214
    return millas



def main():

    k = int(input("Escribe los kilometros "))
    print("La cantitad den millas es: " ,convertirKilometros(k))

main()

