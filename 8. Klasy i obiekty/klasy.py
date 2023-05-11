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

print(czytelnik1.id)
print(czytelnik1.imie)
print(czytelnik1.nazwisko)
print(czytelnik1.wiek)

# w 9 aby zablokowac uzyj __id