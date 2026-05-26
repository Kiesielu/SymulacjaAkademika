from studenci import Kujon, Imprezowicz, Tancerz, Gawendziarz

def test_student_kujon() -> None:
    kujon = Kujon("Olgierd")

    kujon.ucz_sie()
    assert kujon.wiedza == 30
    assert kujon.stres == 10
    assert kujon.spoleczny == 45
    kujon.ucz_sie()
    assert kujon.wiedza == 50
    assert kujon.stres == 20
    assert kujon.spoleczny == 40

def test_student_imprezowicz() -> None:
    imprezowicz = Imprezowicz("Zbyszek")

    imprezowicz.ucz_sie()
    assert imprezowicz.wiedza == 12
    assert imprezowicz.stres == 2
    assert imprezowicz.spoleczny == 65
    imprezowicz.ucz_sie()
    assert imprezowicz.wiedza == 14
    assert imprezowicz.stres == 4
    assert imprezowicz.spoleczny == 80

def test_student_tancerz() -> None:
    tancerz = Tancerz("Anna")

    tancerz.ucz_sie()
    assert tancerz.wiedza == 15
    assert tancerz.stres == 1
    assert tancerz.spoleczny == 60
    tancerz.ucz_sie()
    assert tancerz.wiedza == 20
    assert tancerz.stres == 2
    assert tancerz.spoleczny == 70

def test_student_gawendziarz() -> None:
    gawendziarz = Gawendziarz("Jan")

    gawendziarz.ucz_sie()
    assert gawendziarz.wiedza == 20
    assert gawendziarz.stres == 5
    assert gawendziarz.spoleczny == 55
    gawendziarz.ucz_sie()
    assert gawendziarz.wiedza == 30
    assert gawendziarz.stres == 10
    assert gawendziarz.spoleczny == 60



