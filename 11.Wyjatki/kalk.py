def dodawanie():
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    wynik = liczba1+liczba2
    informacja = f"{liczba1} + {liczba2} = {wynik}"
    return f"Dodaję: {informacja} ", f"Wynik: {wynik}"

def odejmowanie():

    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    wynik = liczba1-liczba2
    informacja = f"{liczba1} - {liczba2} = {wynik}"
    return f"Odejmuję: {informacja} ", f"Wynik: {wynik}"

        
def mnożenie():
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    wynik = liczba1*liczba2
    informacja = f"{liczba1} * {liczba2} = {wynik}"
    return f"Mnożę: {informacja} ", f"Wynik: {wynik}"
def dzielenie():
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    wynik = liczba1/liczba2
    informacja = f"{liczba1} : {liczba2} = {wynik}"
    return f"Dzielę: {informacja} ", f"Wynik: {wynik}"
    

def menu():
    print("[1] Dodawanie")
    print("[2] Odejmowanie")
    print("[3] Mnożenie")
    print("[4] Dzielenie")

menu()
try:
    option = int(input("Co chcesz zrobić[1-4], aby zakończyć działanie programu [0]: "))

    while option != 0:   
        try:
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
        except ValueError:
            print("Wprowadzono nieprawidłowe dane. Proszę wprowadzić liczby!")
        except ZeroDivisionError:
            print("Nie można dzielić przez zero!")
    print("Koniec programu")
except ValueError:
    print("Następnym razem wybierz jedną z opcji: [1], [2], [3], [4], [0]. Program zakończył swoje działanie.")


