class Czytelnik:
    def __init__(self,id,imie,nazwisko,wiek):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

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
print(f"Czytelnik {czytelnik1.id}: ")
print(czytelnik1.id)
print(czytelnik1.imie)
print(czytelnik1.nazwisko)
print(czytelnik1.wiek)
print(f"Czytelnik {czytelnik2.id}: ")
print(czytelnik2.id)
print(czytelnik2.imie)
print(czytelnik2.nazwisko)
print(czytelnik2.wiek)
# w 9 aby zablokowac uzyj __id