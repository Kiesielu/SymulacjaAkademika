from studenci import Student, Kujon, Imprezowicz, Tancerz, Gawendziarz, inicjalizuj_gre


def test_student_initialization():
    inicjalizuj_gre("test_seed")
    student = Student("Testowy")
    assert student.imie == "Testowy"
    assert 10 <= student.wiedza <= 30
    assert 0 <= student.stres <= 20
    assert 10 <= student.spoleczny <= 40
    assert student.indeks is not None
    assert len(student.indeks.oceny) == 0


def test_stat_clamping():
    student = Student("Testowy")

    student.wiedza = 150
    assert student.wiedza == 100

    student.stres = 200
    assert student.stres == 100

    student.spoleczny = 120
    assert student.spoleczny == 100

    student.wiedza = -10
    assert student.wiedza == 0

    student.stres = -50
    assert student.stres == 0

    student.spoleczny = -5
    assert student.spoleczny == 0


def test_kujon_learning():
    kujon = Kujon("Adam")
    kujon.wiedza = 50
    kujon.stres = 30
    kujon.spoleczny = 40

    kujon.ucz_sie()

    assert kujon.wiedza == 70
    assert kujon.stres == 40
    assert kujon.spoleczny == 35


def test_imprezowicz_learning():
    imprezowicz = Imprezowicz("Bartek")
    imprezowicz.wiedza = 50
    imprezowicz.stres = 30
    imprezowicz.spoleczny = 40

    imprezowicz.ucz_sie()

    assert imprezowicz.wiedza == 52
    assert imprezowicz.stres == 32
    assert imprezowicz.spoleczny == 55


def test_tancerz_learning():
    tancerz = Tancerz("Czarek")
    tancerz.wiedza = 50
    tancerz.stres = 30
    tancerz.spoleczny = 40

    tancerz.ucz_sie()

    assert tancerz.wiedza == 55
    assert tancerz.stres == 31
    assert tancerz.spoleczny == 50


def test_gawendziarz_learning():
    gawendziarz = Gawendziarz("Darek")
    gawendziarz.wiedza = 50
    gawendziarz.stres = 30
    gawendziarz.spoleczny = 40

    gawendziarz.ucz_sie()

    assert gawendziarz.wiedza == 60
    assert gawendziarz.stres == 35
    assert gawendziarz.spoleczny == 45
