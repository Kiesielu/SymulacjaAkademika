class Indeks:
    def __init__(self) -> None:
        self.oceny: list[float] = [] #do tworzenia ocen w indeksach studentow

    def dodaj_ocene(self, nowa_ocena: float) -> None:
        self.oceny.append(nowa_ocena)

    def pokaz_srednia(self) -> float:
        if not self.oceny:
            return 0.0

        suma_ocen = sum(self.oceny)
        ilosc_ocen = len(self.oceny)
        return suma_ocen / ilosc_ocen