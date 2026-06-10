import random
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
    stara_funkcja = random.random
    random.random = lambda: 0.1

    student = Kujon("Student")
    student.wiedza = 100
    student.stres = 50

    kolokwium = LosoweKolokwium()
    kolokwium.odpal_dla(student)

    assert student.indeks.oceny == [2]
    random.random = stara_funkcja


def test_kolokwium_zaspanie_not_triggered():
    stara_funkcja = random.random
    random.random = lambda: 0.9

    student = Kujon("Student")
    student.wiedza = 100
    student.stres = 50

    kolokwium = LosoweKolokwium()
    kolokwium.odpal_dla(student)

    assert student.indeks.oceny == [5]
    random.random = stara_funkcja


def test_kolokwium_sciaganie_sukces():
    stara_funkcja = random.random
    random.random = lambda: 0.1

    student = Kujon("Student")
    student.wiedza = 10
    student.spoleczny = 60
    student.stres = 0

    pomocnik = Kujon("KujonPomocnik")
    pomocnik.wiedza = 80

    ekipa = [student, pomocnik]
    kolokwium = LosoweKolokwium()
    kolokwium.odpal_dla(student, ekipa)

    assert student.indeks.oceny == [4]
    random.random = stara_funkcja


def test_kolokwium_sciaganie_zlapanie():
    stara_funkcja = random.random
    random.random = lambda: 0.8

    student = Kujon("Student")
    student.wiedza = 30
    student.spoleczny = 60
    student.stres = 0

    pomocnik = Kujon("KujonPomocnik")
    pomocnik.wiedza = 80

    ekipa = [student, pomocnik]
    kolokwium = LosoweKolokwium()
    kolokwium.odpal_dla(student, ekipa)

    assert student.indeks.oceny == [2]
    random.random = stara_funkcja
