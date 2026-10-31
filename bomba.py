import time

ile = int(input("Podaj czas odliczania bomby "))

licznik = ile

while licznik >= 1:
    print(f"Pozostało {licznik} sekund")
    time.sleep(1)
    licznik -= 1
    if licznik == ile/2:
        print("Minęła połowa czasu. Powinieneś uciekać")
    if licznik == 3:
        print("Pozostały 3 sekundy. Nie powinno cię już tu być!")

print("Planeta unicestwiona")