import tkinter as tk

def dodaj():
    a = float(e1.get())
    b = float(e2.get())
    wynik.config(text=a + b)

def odejmij():
    a = float(e1.get())
    b = float(e2.get())
    wynik.config(text=a - b)

def pomnoz():
    a = float(e1.get())
    b = float(e2.get())
    wynik.config(text=a * b)

def podziel():
    a = float(e1.get())
    b = float(e2.get())

    if b == 0:
        wynik.config(text="blad")
    else:
        wynik.config(text=a / b)

def potega():
    a = float(e1.get())
    b = float(e2.get())
    wynik.config(text=a ** b)

def pierwiastek():
    a = float(e1.get())
    wynik.config(text=a ** 0.5)

def binarna():
    a = int(e1.get())
    wynik.config(text=bin(a))

def hexa():
    a = int(e1.get())
    wynik.config(text=hex(a))


root = tk.Tk()
root.title("Kalkulator")

e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

tk.Button(root, text="Dodaj", command=dodaj).pack()
tk.Button(root, text="Odejmij", command=odejmij).pack()
tk.Button(root, text="Pomnoz", command=pomnoz).pack()
tk.Button(root, text="Podziel", command=podziel).pack()
tk.Button(root, text="Potega", command=potega).pack()
tk.Button(root, text="Pierwiastek", command=pierwiastek).pack()
tk.Button(root, text="Binarnie", command=binarna).pack()
tk.Button(root, text="Hex", command=hexa).pack()

wynik = tk.Label(root, text="Wynik")
wynik.pack()

root.mainloop()