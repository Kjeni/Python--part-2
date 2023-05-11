class Czytelnik:
    def __init__(self,id,imie,nazwisko,wiek):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.__wiek = wiek

def stworz_czytelnika():
    return

def pobierz_wiek(self) -> int:
    return self.__wiek

czytelnik1 = Czytelnik(
    id=1,
    imie = "Kacper",
    nazwisko= "Błażejewski",
    wiek=20
)


print(czytelnik1.id)
print(czytelnik1.imie)
print(czytelnik1.nazwisko)
print(pobierz_wiek(czytelnik1))

