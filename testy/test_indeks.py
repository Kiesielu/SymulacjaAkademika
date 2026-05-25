from indeks import Indeks


def test_indeks() -> None:
    indeks = Indeks()

    indeks.dodaj_ocene(3.0)
    indeks.dodaj_ocene(4.0)
    indeks.dodaj_ocene(5.0)

    assert indeks.pokaz_srednia() == 4.0

    indeks.dodaj_ocene(2.0)
    indeks.dodaj_ocene(2.0)
    indeks.dodaj_ocene(2.0)
    indeks.dodaj_ocene(3.0)
    indeks.dodaj_ocene(3.0)

    assert indeks.pokaz_srednia() == 3.0


def test_indeks2() -> None:
    indeks = Indeks()

    indeks.dodaj_ocene(4.0)
    indeks.dodaj_ocene(5.0)
    indeks.dodaj_ocene(5.0)

    assert round(indeks.pokaz_srednia(), 1) == 4.7


def test_pusty() -> None:
    indeks = Indeks()
    assert indeks.pokaz_srednia() == 0.0
