from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, nazwa):
        self.nazwa = nazwa

        @abstractmethod
        def oblicz_obwod(self):
            pass
        @abstractmethod
        def oblicz_pole(self):
            pass

class Kwadrat(Figura):
    def __init__(self, bok):
        super().__init__("Kwadrat")
        self.bok = bok

    def oblicz_obwod(self):
        return 4 * self.bok

    def oblicz_pole(self):
        return self.bok **2
    
class Kolo(Figura):
    def __init__(self,promien):
        super().__init__("Kolo")
        self.promien = promien

    def oblicz_obwod(self):
        return 3.14 * 2 * self.promien

    def oblicz_pole(self):
        return 3.14 * (self.promien **2)

#przykładowe obliczenia: 
kwadrat = Kwadrat(5)
print(f"Figura: {kwadrat.nazwa}")
print(f"Obwód wynosi: {kwadrat.oblicz_obwod()}")
print(f"Pole wynosi: {kwadrat.oblicz_pole()}")

kolo = Kolo(3)
print(f"Figura: {kolo.nazwa}")
print(f"Obwód wynosi: {kolo.oblicz_obwod()}")
print(f"Pole wynosi: {kolo.oblicz_pole()}")
    
    