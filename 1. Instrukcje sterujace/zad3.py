import random

while True:
    liczba = random.randint(0, 100)
    liczbagracza = int(input("Zgadnij jaką liczę mam na myśli: "))
    count = 0

    while True:
        count += 1
        if liczba > liczbagracza:
            print("Twoja liczba jest mniejsza od mojej!")
            liczbagracza = int(input("Zgadnij jaką liczę mam na myśli: "))
        elif liczba < liczbagracza:
            print("Twoja liczba jest większa od mojej!")
            liczbagracza = int(input("Zgadnij jaką liczę mam na myśli: "))
        else:
            print(f"Brawo udało ci się w {count} strzałach")
            break

    graj_ponownie = input("Czy chcesz zagrać jeszcze raz? (tak/nie): ")

    if graj_ponownie.lower() != "tak":
        break


