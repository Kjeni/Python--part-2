wyraz = input("Podaj słowo: ")
wyraz = wyraz.lower().replace(" "," ")
odwroconywyraz = ""
for index in range(len(wyraz)-1,-1,-1):
    odwroconywyraz += wyraz[index]

if odwroconywyraz == wyraz:
    print("Palidrom")
else:
    print("Nie jest palidromem")