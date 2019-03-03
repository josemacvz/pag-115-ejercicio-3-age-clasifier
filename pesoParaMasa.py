#José Luis Macías grupo 03
#El programa pide la masa al usuario y calcula el peso.

def calcularPeso(m):
    if m * 9.8 > 500:
        return "El objeto es muy pesado"
    else:
        if m * 9.8 < 100:
            return "El objeto es muy ligero"




def main():

    m = int(input("Escribe la masa: "))
    print(calcularPeso(m))


main()
