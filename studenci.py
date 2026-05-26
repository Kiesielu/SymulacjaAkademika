from indeks import Indeks


class Student:
    def __init__(stud, imie: str) -> None:
        stud.imie: str = imie  # disclaimer: imiona zrobimy przez typera
        stud.wiedza: int = 10  # start 10 do max 100
        stud.stres: int = 0  # start 0 do max 100
        stud.indeks: Indeks = Indeks()  # do nadania mu indeksu

    # def logi(stud) -> None:
    # tba trzeba zrobic logi tutaj

    def ucz_sie(stud) -> None:
        stud.wiedza += 10
        stud.stres += 5


class Kujon(Student):
    def ucz_sie(stud) -> None:
        stud.wiedza += 20
        stud.stres += 10


class Imprezowicz(Student):
    def ucz_sie(stud) -> None:
        stud.wiedza += 2
        stud.stres += 2


class Tancerz(Student):
    def ucz_sie(stud) -> None:
        stud.wiedza += 5
        stud.stres += 1


class Gawendziarz(Student):
    pass
