import random
from alkohole import Piwo, Wino, Wodka, Bimber


class LosowaImpreza:
    def odpal_dla(wyd, stud, ekipa=None):
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
    def odpal_dla(wyd, stud, ekipa=None):
        stud.stres += 35

        if stud.stres >= 80 and random.random() < 0.5:
            ocena = 2
        else:
            if stud.wiedza >= 40:
                ocena = 5
            elif stud.wiedza >= 20:
                ocena = 3
            else:
                ocena = 2

            # Ściąganie: towarzyskość >= 50, niska własna ocena i obecność pomocnych kolegów
            if ocena < 5 and stud.spoleczny >= 50 and ekipa:
                pomocnicy = [s for s in ekipa if s != stud and s.wiedza >= 40]
                if pomocnicy:
                    helper = random.choice(pomocnicy)
                    # 70% szans na powodzenie ściągania, 30% szans na przyłapanie
                    if random.random() < 0.7:
                        ocena = 4
                    else:
                        ocena = 2

        stud.indeks.dodaj_ocene(ocena)
