nrLini = int(input("Podaj numer lini: "))
cenaBiletu = float(input("Podaj cenę biletu: "))
progRuchu = int(input("Podaj próg dużego ruchu: "))
liczbaPasazerow = input("Podaj liczbę pasażerów z 7 dni tygodnia: ")

dni = ["pon", "wt", "śr", "czw", "pt", "sb", "nd"]

pasazerowie = []

for element in liczbaPasazerow.split():
    osoba = element.split(" ")
    pasazerowie.append(int(osoba[0]))


if(len(pasazerowie) != 7):
    print("Nieodpowidnia liczba pasażerów")
else:
    print(f"<------------RAPORT TYGODNIOWY LINI {nrLini}----------->")

    for i in range(len(dni)):
        if(pasazerowie[i] > progRuchu):
            print(dni[i], ":", pasazerowie[i], "pasażerów <-------DUŻY RUCH")
        else:
            print(dni[i], ":", pasazerowie[i], "pasażerów")

    suma = 0
    sumaBiletow = 0

    for i in range(len(dni)):
        suma += pasazerowie[i]
        sumaBiletow += cenaBiletu

    srednia = suma/len(dni)

    print("Pasażerowie w tygodniu:", suma)
    print(f"Średnia pasażerów: {srednia:.2f} zł")
    print("Przychód z biletów:", sumaBiletow)

    najwiecej = 0

    for i in range(len(dni)):
        if(pasazerowie[i] > srednia):
            najwiecej += 1

    print("Dni z dużym ruchem:", najwiecej)

