from verkiezing import Kandidaat, Stem, Kiezer

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self._opleiding = opleiding

    @property
    def opleiding(self):
        return self._opleiding

    def __str__(self):
        return f"{self.naam} ({self.opleiding})"

class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self.opleiding})"

class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self._opleiding = opleiding

    @property
    def opleiding(self):
        return self._opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.opleiding:
            stem = DecaanStem(kandidaat, self.opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} ({self.opleiding})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")

# ============================
# Stemronde (onderaan laten)
# ============================

if __name__ == "__main__":
    kandidaten = [
        DecaanKandidaat("Emma", "Informatica"),
        DecaanKandidaat("Milan", "Economie")
    ]

    kiezers = [
        DecaanKiezer("Tara", "Informatica"),
        DecaanKiezer("Noor", "Informatica"),
        DecaanKiezer("Ben", "Economie"),
        DecaanKiezer("Julie", "Geneeskunde")  # ongeldig
    ]

    for kiezer in kiezers:
        for kandidaat in kandidaten:
            kiezer.stem(kandidaat)

    print("\n--- Uitslag Decaanverkiezing ---")
    for kandidaat in kandidaten:
        print(f"{kandidaat}: {kandidaat.aantal_stemmen} stemmen")
