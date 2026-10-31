import tkinter as tk

def dodaj(a, b):
    wynik.config(text=str(a + b))

def odejmij(a, b):
    wynik.config(text=str(a - b))

def pomnoz(a, b):
    wynik.config(text=str(a * b))

def podziel(a, b):
    wynik.config(text=str(a / b))

def poteguj(a):
    wynik.config(text=str(a * a))

root = tk.Tk()
root.title("Kalkulator")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

if dodaj:
    button = tk.Button(root, text="Dodaj", command=dodaj)
    button.pack()

    wynik = tk.Label(root, text="Wynik")
    wynik.pack()
elif odejmij:
    button = tk.Button(root, text="Odejmij", command=odejmij)
    button.pack()

    wynik = tk.Label(root, text="Wynik")
    wynik.pack()
elif pomnoz:
    button = tk.Button(root, text="Dodaj", command=pomnoz)
    button.pack()

    wynik = tk.Label(root, text="Wynik")
    wynik.pack()
elif podziel:
    button = tk.Button(root, text="Dodaj", command=podziel)
    button.pack()

    wynik = tk.Label(root, text="Wynik")
    wynik.pack()
elif poteguj:
    button = tk.Button(root, text="Dodaj", command=poteguj)
    button.pack()

    wynik = tk.Label(root, text="Wynik")
    wynik.pack()


root.mainloop()