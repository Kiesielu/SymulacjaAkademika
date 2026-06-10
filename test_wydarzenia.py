from studenci import Kujon, inicjalizuj_gre
from wydarzenia import LosowaImpreza, LosoweKolokwium


def test_impreza():
    inicjalizuj_gre("test")
    student = Kujon("Student")
    student.wiedza = 50

    impreza = LosowaImpreza()
    impreza.odpal_dla(student)

    assert student.wiedza < 50


def test_kolokwium():
    student = Kujon("Student")
    student.wiedza = 50
    student.stres = 0

    kolokwium = LosoweKolokwium()
    kolokwium.odpal_dla(student)

    assert student.stres == 35
    assert student.indeks.oceny == [5]


def test_kolokwium_zaspanie_triggered():
    from unittest.mock import patch
    student = Kujon("Student")
    student.wiedza = 100
    student.stres = 50  # 50 + 35 = 85 (>= 80)

    kolokwium = LosoweKolokwium()
    with patch("random.random", return_value=0.1):  # < 0.5 -> triggers oversleeping
        kolokwium.odpal_dla(student)

    assert student.indeks.oceny == [2]


def test_kolokwium_zaspanie_not_triggered():
    from unittest.mock import patch
    student = Kujon("Student")
    student.wiedza = 100
    student.stres = 50  # 85 (>= 80)

    kolokwium = LosoweKolokwium()
    with patch("random.random", return_value=0.9):  # >= 0.5 -> no oversleeping
        kolokwium.odpal_dla(student)

    assert student.indeks.oceny == [5]


def test_kolokwium_sciaganie_sukces():
    from unittest.mock import patch
    student = Kujon("Student")
    student.wiedza = 10  # normal grade 2
    student.spoleczny = 60  # >= 50, wants to cheat
    student.stres = 0

    pomocnik = Kujon("KujonPomocnik")
    pomocnik.wiedza = 80  # helper >= 40

    ekipa = [student, pomocnik]
    kolokwium = LosoweKolokwium()

    # Since stress < 80, the first random.random() check for oversleeping is short-circuited.
    # random.random() is called only once for the cheating check.
    with patch("random.random", return_value=0.1):  # < 0.7 -> successfully cheats
        kolokwium.odpal_dla(student, ekipa)

    assert student.indeks.oceny == [4]  # grade boosted to 4


def test_kolokwium_sciaganie_zlapanie():
    from unittest.mock import patch
    student = Kujon("Student")
    student.wiedza = 30  # normal grade 3
    student.spoleczny = 60  # >= 50, wants to cheat
    student.stres = 0

    pomocnik = Kujon("KujonPomocnik")
    pomocnik.wiedza = 80  # helper >= 40

    ekipa = [student, pomocnik]
    kolokwium = LosoweKolokwium()

    with patch("random.random", return_value=0.8):  # >= 0.7 -> gets caught
        kolokwium.odpal_dla(student, ekipa)

    assert student.indeks.oceny == [2]  # grade dropped/kept to 2 because got caught

