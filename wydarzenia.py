import random
from alkohole import Piwo, Wodka, Bimber


class LosowaImpreza:
    def odpal_dla(wyd, stud):
        alko = random.choice(
            [Piwo("Sok Jablkowy"), Wodka("Woda"), Bimber("Sok Pomaranczowy")]
        )
        alko.wypij_przez(stud)

        stud.wiedza -= alko.moc * 5
        if stud.wiedza < 0:
            stud.wiedza = 0


class LosoweKolokwium:
    def odpal_dla(wyd, stud):
        stud.stres += 35
        if stud.stres > 100:
            stud.stres = 100

        if stud.wiedza >= 40:
            ocena = 5
        elif stud.wiedza >= 20:
            ocena = 3
        else:
            ocena = 2

        stud.indeks.oceny.append(ocena)
