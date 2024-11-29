import random

lista = []
for i in range(3):
    fakty = input("podaj fakt o sobie")
    lista.append(fakty)
print("twój losowy fakt to:", random.choice(lista))
