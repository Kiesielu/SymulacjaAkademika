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
