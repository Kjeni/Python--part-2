from os import path
import string

def policz_slowa(tekst):
    tekst = tekst.translate(str.maketrans('', '', string.punctuation))
    slowa = tekst.split()
    liczba_slow = len(slowa)
    
#stats
    statystyki = {}
    for slowo in slowa:
        litera_koncowa = slowo[-1]
        if litera_koncowa in statystyki:
            statystyki[litera_koncowa] += 1
        else:
            statystyki[litera_koncowa] = 1
    
    return liczba_slow, statystyki

dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

with open(data_path, 'r') as file:
    tekst = file.read()

liczba_slow, statystyki = policz_slowa(tekst)

print("Liczba słów: ", liczba_slow)
print("Statystyki, litery kończące słowa: ")
for litera, liczba in statystyki.items():
    print(f"{litera}: {liczba}")
