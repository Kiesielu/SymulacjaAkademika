"""Klasy studentow bioracych udzial w symulacji."""

import random
from indeks import Indeks


def inicjalizuj_gre(podany_seed=None) -> None:
    """Inicjalizacja generatora losowego."""
    if podany_seed is not None:
        random.seed(podany_seed)
    else:
        random.seed()


class Student:
    """Klasa bazowa dla studenta."""

    def __init__(stud, imie: str) -> None:
        """Ustawienie domyslnych statystyk studenta."""
        stud.imie: str = imie
        stud._wiedza: int = random.randint(10, 30)
        stud._stres: int = random.randint(0, 20)
        stud._spoleczny: int = random.randint(10, 40)
        stud.indeks: Indeks = Indeks()
        stud.lista_logow: list[str] = []

    def logi(stud) -> None:
        """Wypisuje logi studenta."""
        for wpis in stud.lista_logow:
            print(f"  {wpis}")

    @property
    def wiedza(stud) -> int:
        """Zwraca poziom wiedzy."""
        return stud._wiedza

    @wiedza.setter
    def wiedza(stud, wartosc: int) -> None:
        """Ustawia poziom wiedzy (zakres 0-100)."""
        stud._wiedza = max(0, min(100, wartosc))

    @property
    def stres(stud) -> int:
        """Zwraca poziom stresu."""
        return stud._stres

    @stres.setter
    def stres(stud, wartosc: int) -> None:
        """Ustawia poziom stresu (zakres 0-100)."""
        stud._stres = max(0, min(100, wartosc))

    @property
    def spoleczny(stud) -> int:
        """Zwraca poziom towarzyskosci."""
        return stud._spoleczny

    @spoleczny.setter
    def spoleczny(stud, wartosc: int) -> None:
        """Ustawia poziom towarzyskosci (zakres 0-100)."""
        stud._spoleczny = max(0, min(100, wartosc))

    def ucz_sie(stud) -> None:
        """Zwykla nauka studenta."""
        stud.wiedza += 10
        stud.stres += 5
        stud.spoleczny += 5
        stud.lista_logow.append(
            f"Nauka: wiedza={stud.wiedza}, stres={stud.stres}, spoleczny={stud.spoleczny}"
        )


class Kujon(Student):
    """Student typu Kujon."""

    def ucz_sie(stud) -> None:
        """Nauka kujona - duzo wiedzy i stresu, malo towarzyskosci."""
        stud.wiedza += 20
        stud.stres += 10
        stud.spoleczny -= 5
        stud.lista_logow.append(
            f"Nauka (Kujon): wiedza={stud.wiedza}, stres={stud.stres}, spoleczny={stud.spoleczny}"
        )


class Imprezowicz(Student):
    """Student typu Imprezowicz."""

    def ucz_sie(stud) -> None:
        """Nauka imprezowicza - malo wiedzy, duzo towarzyskosci."""
        stud.wiedza += 2
        stud.stres += 2
        stud.spoleczny += 15
        stud.lista_logow.append(
            f"Nauka (Imprezowicz): wiedza={stud.wiedza}, stres={stud.stres}, spoleczny={stud.spoleczny}"
        )


class Tancerz(Student):
    """Student typu Tancerz."""

    def ucz_sie(stud) -> None:
        """Nauka tancerza - srednie statystyki."""
        stud.wiedza += 5
        stud.stres += 1
        stud.spoleczny += 10
        stud.lista_logow.append(
            f"Nauka (Tancerz): wiedza={stud.wiedza}, stres={stud.stres}, spoleczny={stud.spoleczny}"
        )


class Gawendziarz(Student):
    """Student typu Gawendziarz."""

    pass
