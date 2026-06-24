"""Glowny plik do uruchamiania symulacji."""

import sys
from silnik import SilnikSymulacji
from studenci import inicjalizuj_gre


def main():
    """Funkcja glowna parsujaca argumenty i startujaca symulacje."""
    ilosc_dni = 30
    seed = None

    if len(sys.argv) > 1:
        try:
            ilosc_dni = int(sys.argv[1])
        except ValueError:
            pass

    if len(sys.argv) > 2:
        seed = sys.argv[2]

    inicjalizuj_gre(seed)

    symulator = SilnikSymulacji()
    symulator.odpal_symulacje(ilosc_dni=ilosc_dni)


if __name__ == "__main__":
    main()