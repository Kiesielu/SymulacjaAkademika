"""Klasa indeksu studenta."""


class Indeks:
    """Reprezentuje indeks z ocenami."""

    def __init__(stud) -> None:
        """Tworzy pusty indeks."""
        stud.oceny: list[float] = []

    def dodaj_ocene(stud, nowa_ocena: float) -> None:
        """Dodaje nowa ocene."""
        stud.oceny.append(nowa_ocena)

    def pokaz_srednia(stud) -> float:
        """Liczy srednia ocen."""
        if not stud.oceny:
            return 0.0

        suma_ocen = sum(stud.oceny)
        ilosc_ocen = len(stud.oceny)
        return suma_ocen / ilosc_ocen
