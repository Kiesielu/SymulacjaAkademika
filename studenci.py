from indeks import Indeks

def inicjalizuj_gre(podany_seed=None) -> None:
    if podany_seed is not None:
        random.seed(podany_seed)
    else:
        random.seed()

class Student:
    def __init__(stud, imie: str) -> None:
        stud.imie: str = imie  # disclaimer: imiona zrobimy przez typera

        stud.wiedza: int = random.randint(10, 30)  # start 10 do max 100
        stud.stres: int = random.randint(0, 20)  # start 0 do max 100
        stud.spoleczny: int = random.randint(10, 40)
        stud.indeks: Indeks = Indeks()  # do nadania mu indeksu

    # def logi(stud) -> None:
    # tba trzeba zrobic logi tutaj

    def ucz_sie(stud) -> None:
        stud.wiedza += 10
        stud.stres += 5
        stud.spoleczny += 5


class Kujon(Student):
    def ucz_sie(stud) -> None:
        stud.wiedza += 20
        stud.stres += 10
        stud.spoleczny -= 5  # wiadomo siedzi w domu i sie tylko uczy hehe


class Imprezowicz(Student):
    def ucz_sie(stud) -> None:
        stud.wiedza += 2
        stud.stres += 2
        stud.spoleczny += 15


class Tancerz(Student):
    def ucz_sie(stud) -> None:
        stud.wiedza += 5
        stud.stres += 1
        stud.spoleczny += 10


class Gawendziarz(Student):
    pass
