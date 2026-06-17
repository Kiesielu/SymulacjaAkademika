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
        stud.lista_logow.append(f"Impreza - wybrano: {alko.nazwa}")
        alko.wypij_przez(stud)
        stud.wiedza -= alko.moc * 5


class LosoweKolokwium:
    def odpal_dla(wyd, stud, ekipa=None):
        stud.stres += 35

        if stud.stres >= 80 and random.random() < 0.5:
            ocena = 2
            stud.lista_logow.append(f"Kolokwium: zaspanie z powodu stresu, ocena={ocena}")
        else:
            if stud.wiedza >= 40:
                ocena = 5
            elif stud.wiedza >= 20:
                ocena = 3
            else:
                ocena = 2

            sciaganie = False
            if ocena < 5 and stud.spoleczny >= 50 and ekipa is not None:
                pomocnicy = []
                for s in ekipa:
                    if s != stud and s.wiedza >= 40:
                        pomocnicy.append(s)

                if len(pomocnicy) > 0:
                    sciaganie = True
                    helper = random.choice(pomocnicy)
                    if random.random() < 0.7:
                        ocena = 4
                        stud.lista_logow.append(f"Kolokwium: sciaganie od {helper.imie}, ocena={ocena}")
                    else:
                        ocena = 2
                        stud.lista_logow.append(f"Kolokwium: przylapany na sciaganiu od {helper.imie}, ocena={ocena}")

            if not sciaganie:
                stud.lista_logow.append(f"Kolokwium: napisane samodzielnie, ocena={ocena}")

        stud.indeks.dodaj_ocene(ocena)
