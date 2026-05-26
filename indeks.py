class Indeks:
    def __init__(stud) -> None:
        stud.oceny: list[float] = []  # do tworzenia ocen w indeksach studentow

    def dodaj_ocene(stud, nowa_ocena: float) -> None:
        stud.oceny.append(nowa_ocena)

    def pokaz_srednia(stud) -> float:
        if not stud.oceny:
            return 0.0

        suma_ocen = sum(stud.oceny)
        ilosc_ocen = len(stud.oceny)
        return suma_ocen / ilosc_ocen
