from abc import ABC, abstractmethod

# Abstracte basisklasse
class Persoon(ABC):
    def __init__(self, naam):
        self._naam = naam

    @property
    def naam(self):
        return self._naam

    @abstractmethod
    def __str__(self):
        pass

class Kandidaat(Persoon):
    def __init__(self, naam):
        super().__init__(naam)
        self._stemmen = []

    def geef_stem(self, stem):
        self._stemmen.append(stem)

    @property
    def aantal_stemmen(self):
        return len(self._stemmen)

    def __str__(self):
        return f"{self.naam}"

class Stem:
    def __init__(self, kandidaat):
        self.kandidaat = kandidaat

    def __str__(self):
        return f"Stem op {self.kandidaat}"

class Kiezer(Persoon):
    def __init__(self, naam):
        super().__init__(naam)

    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self.naam} heeft gestemd op {kandidaat}")

    def __str__(self):
        return self.naam
