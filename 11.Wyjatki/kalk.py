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


while True:
    menu()
    option = input("Co chcesz zrobić [1-4], aby zakończyć działanie programu [0]: ")

    try:
        option = int(option)  # Konwertujemy wprowadzoną wartość na liczbę całkowitą

        if option not in [1, 2, 3, 4, 0]:
            print("Wprowadź poprawną wartość [1], [2], [3], [4] lub [0]")
            continue
        if option == 0:
            break
        if option == 1:
            print(dodawanie())
        elif option == 2:
            print(odejmowanie())
        elif option == 3:
            print(mnożenie())
        elif option == 4:
            print(dzielenie())

    except ValueError:
        print("Wprowadzono nieprawidłowe dane. Proszę wprowadzać liczby!")
    except ZeroDivisionError:
        print("Nie można dzielić przez zero!")

print("Koniec programu")

