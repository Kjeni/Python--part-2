from os import path
import random
import os

# Funkcja do generowania kombinacji imion i nazwisk
def generuj_kombinacje(imiona, nazwiska, liczba_kombinacji):
    kombinacje = random.sample(list(zip(imiona, nazwiska)), liczba_kombinacji)
    return kombinacje


dir_path = path.dirname(__file__)
filename = "imiona.txt"
data_path1 = path.join(dir_path, filename)
if not os.path.exists(data_path1):
    print("Brak pliku z imionami")
    exit()
with open(data_path1, 'r', encoding='utf-8') as file:
    imiona = file.read().splitlines()
    imiona = [imie.lower().capitalize() for imie in imiona]


dir_path = path.dirname(__file__)
filename = "nazwiska.txt"
data_path2 = path.join(dir_path, filename)
if not os.path.exists(data_path2):
    print("Brak pliku z nazwiskami")
    exit()
    
with open(data_path2, 'r', encoding='utf-8') as file:
    nazwiska = file.read().splitlines()
    nazwiska = [nazwisko.lower().capitalize() for nazwisko in nazwiska]


liczba_kombinacji = int(input("Podaj liczbę kombinacji do wygenerowania: "))


kombinacje = generuj_kombinacje(imiona, nazwiska, liczba_kombinacji)

dir_path = path.dirname(__file__)
filename = "kombinacje.txt"
data_path3 = path.join(dir_path, filename)
with open(data_path3, 'w', encoding='utf-8') as file:
    for kombinacja in kombinacje:
        imie, nazwisko = kombinacja
        file.write(f"{imie} {nazwisko}\n")

print(f"Generowanie i zapisywanie {liczba_kombinacji} kombinacji zakończone.")
