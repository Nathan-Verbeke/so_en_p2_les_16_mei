from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self._faculteit = faculteit

    @property
    def faculteit(self):
        return self._faculteit

    def __str__(self):
        return f"{self.naam} (Rector: {self.faculteit})"

class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.faculteit = faculteit

    def __str__(self):
        return f"Stem op {self.kandidaat} (Rector: {self.faculteit})"

# ============================
# Stemronde (kan onderaan script blijven)
# ============================

if __name__ == "__main__":
    kandidaten = [
        RectorKandidaat("Sarah", "Letteren"),
        RectorKandidaat("Jonas", "Wetenschappen")
    ]

    kiezers = [
        Kiezer("Leen"),
        Kiezer("Sven"),
        Kiezer("Ahmed")
    ]

    for kiezer in kiezers:
        kiezer.stem(kandidaten[0])  # Alle stemmen naar Sarah

    print("\n--- Uitslag Rectorverkiezing ---")
    for kandidaat in kandidaten:
        print(f"{kandidaat}: {kandidaat.aantal_stemmen} stemmen")