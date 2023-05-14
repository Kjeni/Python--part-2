class Czytelnik:
    def __init__(self,id,imie,nazwisko,wiek):
        self.__id = id
        self.imie = imie
        self.__nazwisko = nazwisko
        self.__wiek = wiek

def pobierz_wiek(self) -> int:
    return self.__wiek
def pobierz_imie(self) -> str:
    return self.imie

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

print(pobierz_imie(czytelnik1))
print(pobierz_wiek(czytelnik1))

