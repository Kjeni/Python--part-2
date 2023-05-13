class Czytelnik:
    def __init__(self,id,imie,nazwisko,wiek):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.__wiek = wiek

def pobierz_wiek(self) -> int:
    return self.__wiek

czytelnik1 = Czytelnik(
    id=1,
    imie = "Kacper",
    nazwisko= "Błażejewski",
    wiek=20
)
czytelnik2 = Czytelnik(
    id=2,
    imie = "Kamil",
    nazwisko= "Kurczak",
    wiek=22
)

print(pobierz_wiek(czytelnik1))
print(pobierz_wiek(czytelnik2))

