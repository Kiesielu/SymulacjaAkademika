import random
from alkohole import Piwo, Wino, Wodka, Bimber


class LosowaImpreza:
    def odpal_dla(wyd, stud):
        alko = random.choice(
            [
                Piwo("Sok Jablkowy"),
                Wino("Kompot"),
                Wodka("Woda"),
                Bimber("Sok Pomaranczowy"),
            ]
        )
        alko.wypij_przez(stud)

        stud.wiedza -= alko.moc * 5


class LosoweKolokwium:
    def odpal_dla(wyd, stud):
        stud.stres += 35

        if stud.wiedza >= 40:
            ocena = 5
        elif stud.wiedza >= 20:
            ocena = 3
        else:
            ocena = 2

        stud.indeks.dodaj_ocene(ocena)
