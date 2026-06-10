import random
from studenci import Gawendziarz, Imprezowicz, Kujon, Tancerz
from wydarzenia import LosowaImpreza, LosoweKolokwium


class SilnikSymulacji:

    def __init__(self):
        self.ekipa = [
            Kujon("Kujon"),
            Imprezowicz("Imprezowicz"),
            Gawendziarz("Gawendziarz"),
            Tancerz("Tancerz"),
        ]
        self.wydarzenia = [LosowaImpreza(), LosoweKolokwium()]

    def pokaz_stan(self):
        print("statystki studentow")
        for s in self.ekipa:
            print(
                f"Imie: {s.imie} | Wiedza: {s.wiedza} | Stres: {s.stres} | Oceny: {s.indeks.oceny}"
            )

    def symuluj_dzien(self, numer_dnia):
        print(f"dzien nr: {numer_dnia}")

        akcja = random.choice(["nauka", "odpoczynek"])

        if akcja == "nauka":
            print("Dzisiaj nauka")
            for s in self.ekipa:
                s.ucz_sie()
        else:
            print("Dzisiaj luzny dzien")

        if random.choice([True, False]):
            wydarzenie = random.choice(self.wydarzenia)
            print(
                f"losowe wydarzenie: {wydarzenie.__class__.__name__}!"
            )
            for s in self.ekipa:
                wydarzenie.odpal_dla(s)

    def odpal_symulacje(self, ilosc_dni):
        for i in range(1, ilosc_dni + 1):
            self.symuluj_dzien(i)
            self.pokaz_stan()