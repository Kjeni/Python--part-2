import random
liczba = random.randint(0,101)
# print(liczba)
liczbagracza = int(input("Zgadnij jaką liczę mam na myśli: "))
count = 0
while True:
    count += 1
    if liczba > liczbagracza:
        print("Twoja liczba jest mniejsza od mojej!")
        liczbagracza= int(input("Zgadnij jaką liczę mam na myśli: "))
    elif liczba < liczbagracza:
        print("Twoja liczba jest większa od mojej!")
        liczbagracza= int(input("Zgadnij jaką liczę mam na myśli: "))
    else:
        print(f"Brawo udało ci się w {count} strzałach")
        break


