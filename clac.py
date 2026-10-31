def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pomnoz(x, y):
    return x * y

def podziel(x, y):
    if y == 0:
        return "Błąd: Dzielenie przez zero!"
    return x / y

print("Wybierz operację:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

while True:
    wybor = input("Wpisz numer operacji (1/2/3/4): ")

    if wybor in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Wprowadź pierwszą liczbę: "))
            num2 = float(input("Wprowadź drugą liczbę: "))
        except ValueError:
            print("Niepoprawne dane. Wprowadź liczby.")
            continue

        if wybor == '1':
            print(num1, "+", num2, "=", dodaj(num1, num2))
        elif wybor == '2':
            print(num1, "-", num2, "=", odejmij(num1, num2))
        elif wybor == '3':
            print(num1, "*", num2, "=", pomnoz(num1, num2))
        elif wybor == '4':
            print(num1, "/", num2, "=", podziel(num1, num2))
        
        # Pytanie o kolejną operację
        nastepna_operacja = input("Czy chcesz wykonać kolejną operację? (tak/nie): ")
        if nastepna_operacja.lower() != 'tak':
            break
    else:
        print("Niepoprawny wybór operacji. Spróbuj ponownie.")