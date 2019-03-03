#José Luis Macías grupo 03
#El programa preguntará la edad y dirá si es un infante, un niño, un adolescente o mayor.

def esInfante(e):
    if e > 0 and e <= 1:
        personaClasi = str("infante")
        return personaClasi
    else:
        if e > 1 and e < 13:
            personaClasi = str("niño")
            return personaClasi
        else:
            if e >= 13 and e < 20:
                personaClasi = str("adolescente")
                return personaClasi
            else:
                if e >= 20:
                    personaClasi = str("adulto")
                    return personaClasi



def main():

    e = int(input("Escriba la edad de la persona en años: "))
    personaClasi = esInfante(e)
    print("La persona es: ", personaClasi)

main()
