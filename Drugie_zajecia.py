import random

imie = input("Podaj imie: ")

print(f"\nWitaj w grze {imie}!")
print("Znalazłeś się na gorącej pustyni pełnej roznego rodzaju potworow. Strzez sie!")
ilosc_wody_z_kaktusow = 2 #limit do zrobienia
zdrowie_gracza = 100
zdrowie_skorpiona = 50
print("Uwaga nadchodza potwory")

while zdrowie_gracza>0 and zdrowie_skorpiona>0:
    print("Co chcesz zrobic?")
    print("'1' - mocny cios") 
    print("'2'- ulecz sie") 
    wybor = input("Twoja akcja: ")
    
    #tura gracza
    if wybor == "1":
        obrazenia = random.randint(8, 20)
        zdrowie_skorpiona -= obrazenia
        print(f"Uderzyles skorpiona za {obrazenia} teraz skorpion ma {zdrowie_skorpiona} hp.")
    elif wybor == "2":
        print("Leczysz sie za 20 pkt")
        ilosc_wody_z_kaktusow -= 1
        zdrowie_gracza += 20
    else:
        print("zly wybor tracisz ture")
    
    
    #tura przeciwnika
    if zdrowie_skorpiona>0:
        zdrowie_gracza -= random.randint(10, 18)
        print(f"Uderza cie skorpion. Zostalo ci {zdrowie_gracza} hp.")

if zdrowie_skorpiona<1 :
    print("Wygrywasz") 
else:
    print("Przegrywasz")