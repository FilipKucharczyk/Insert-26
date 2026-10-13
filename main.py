import random
import time
zmienna1 = 1
wiek = 21
imie = "Krystian"

#print("Nazywam sie", imie, "Zyje w", wiek, "wieku")
#print("Mam na imie "+imie)
#print("Mam " + str(wiek) + " lat.")
lista_znakow = ["k", "p", "n"]
print("Podaj swoj typ (k - kamien, p-papier, n-nozyce):")
nasz_znak = input()
znak_komputera = random.choice(lista_znakow)
print(znak_komputera)

if (nasz_znak == "k" and znak_komputera == "n") or \
   (nasz_znak == "n" and znak_komputera == "p") or \
   (nasz_znak == "p" and znak_komputera == "k"):
    print("Wygrałeś!")

elif nasz_znak == znak_komputera:
    print("Remis")

else:
    print("Przegrales :(")