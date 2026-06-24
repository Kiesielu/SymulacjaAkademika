"""Klasa silnika symulacji."""

import random
import os
import datetime
from studenci import Gawendziarz, Imprezowicz, Kujon, Tancerz
from wydarzenia import LosowaImpreza, LosoweKolokwium


class SilnikSymulacji:
    """Klasa glowna odpowiadajaca za przeprowadzenie symulacji."""

    def __init__(self):
        """Inicjalizacja studentow, wydarzen oraz sciezki do zapisu logow."""
        self.ekipa = [
            Kujon("Kujon"),
            Imprezowicz("Imprezowicz"),
            Gawendziarz("Gawendziarz"),
            Tancerz("Tancerz"),
        ]
        self.wydarzenia = [LosowaImpreza(), LosoweKolokwium()]

        teraz = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.sciezka_logow = os.path.join("logi", teraz)
        os.makedirs(self.sciezka_logow, exist_ok=True)
        self.plik_logu = os.path.join(self.sciezka_logow, "logi.txt")

    def pokaz_stan(self):
        """Wypisuje statystyki studentow na ekran."""
        print("statystki studentow")
        for s in self.ekipa:
            print(
                f"Imie: {s.imie} | Wiedza: {s.wiedza} | Stres: {s.stres} | Oceny: {s.indeks.oceny}"
            )

    def symuluj_dzien(self, numer_dnia):
        """Symuluje pojedynczy dzien i zapisuje logi do pliku logi.txt."""
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
            print(f"losowe wydarzenie: {wydarzenie.__class__.__name__}!")
            for s in self.ekipa:
                wydarzenie.odpal_dla(s, self.ekipa)

        with open(self.plik_logu, "a", encoding="utf-8") as f:
            log_header = f"--- Dzien {numer_dnia} ---"
            print(log_header)
            f.write(log_header + "\n")

            for s in self.ekipa:
                if len(s.lista_logow) > 0:
                    header = f"  {s.imie}:"
                    print(header)
                    f.write(header + "\n")
                    for wpis in s.lista_logow:
                        print(f"    {wpis}")
                        f.write(f"    {wpis}\n")
                    s.lista_logow.clear()
            f.write("\n")

    def odpal_symulacje(self, ilosc_dni):
        """Uruchamia glowna petle symulacji."""
        for i in range(1, ilosc_dni + 1):
            self.symuluj_dzien(i)
            self.pokaz_stan()
