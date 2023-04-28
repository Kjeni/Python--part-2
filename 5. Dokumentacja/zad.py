def dodawanie():
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
    wynik = liczba1+liczba2
    return wynik
def odejmowanie():
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
    wynik = liczba1-liczba2
    return wynik
def mnożenie():
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
    wynik = liczba1*liczba2
    return wynik
def dzielenie():
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
    wynik = liczba1/liczba2
    return wynik
def menu():
    print("[1] Dodawanie")
    print("[2] Odejmowanie")
    print("[3] Mnożenie")
    print("[4] Dzielenie")

menu()
option = int(input("Co chcesz zrobić[1-4], aby zakończyć działanie programu [0]: "))
while option != 0:
    if option ==1:
        print(dodawanie())
        option = int(input("Co chcesz zrobić[1-4]: "))
    elif option==2:
        print(odejmowanie())
        option = int(input("Co chcesz zrobić[1-4]: "))
    elif option == 3:
        print(mnożenie())
        option = int(input("Co chcesz zrobić[1-4]: "))
    elif option==4:
        print(dzielenie())
        option = int(input("Co chcesz zrobić[1-4]: "))
    elif option==0:
        break
print("Koniec programu")