wiek = int(input("Podaj swój wiek: "))
category_A2 = int(input("Ile lat posiadasz prawo jazdy kategorii A2? (Jeśli nie posiadasz wpisz 0): "))

if wiek >= 24:
    print("Możesz przystąpić do egzaminu na prawo jazdy kategorii A.")
elif category_A2 >= 2 and wiek >= 20:
    print("Możesz przystąpić do egzaminu na prawo jazdy kategorii A.")
else:
    print("Nie spełniasz warunków do przystąpienia do egzaminu na prawo jazdy kategorii B.")
