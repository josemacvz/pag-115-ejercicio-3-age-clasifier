#José Luis Macías grupo 03
#El programa pide una mes, día y año, si el mes multiplicado por el día es igual al año dirá "es una fecha mágica".

def esMagico(m,d,a):

    if m * d == a:
        return "El día de su nacimiento es un día mágico"
    else:
        return "El día de su nacimiento es un gran día"


def main():


    m = int(input("Escriba el mes de su nacimientio en forma numérica: "))
    d = int(input("Escriba el día: "))
    a = int(input("Escriba el año en dos dígitos: "))
    print(esMagico(m,d,a))

main()
