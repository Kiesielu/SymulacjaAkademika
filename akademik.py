from silnik import SilnikSymulacji
from studenci import inicjalizuj_gre


def main():
    inicjalizuj_gre()

    symulator = SilnikSymulacji()
    symulator.odpal_symulacje(ilosc_dni=30)


if __name__ == "__main__":
    main()