from business import Azioni

print("Cosa vuoi vedere?")
scelta = int(input("1. Attori \n2. Film \n3. Esci \n"))

match scelta:

    case 1:
            
        print(Azioni.Film())

    case 2:

        print(Azioni.Attori())
