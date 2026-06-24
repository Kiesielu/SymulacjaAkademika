"""Klasy reprezentujace rozne alkohole."""


class Alkohol:
    """Klasa bazowa dla alkoholi."""

    def __init__(alko, nazwa, moc):
        """Ustawia nazwe i moc alkoholu."""
        alko.nazwa = nazwa
        alko.moc = moc

    def wypij_przez(alko, stud):
        """Zmienia statystyki studenta po wypiciu."""
        stud.stres -= alko.moc * 2
        stud.spoleczny += alko.moc * 3


class Piwo(Alkohol):
    """Klasa dla piwa."""

    def __init__(alko, nazwa):
        super().__init__(nazwa, moc=1)


class Wino(Alkohol):
    """Klasa dla wina."""

    def __init__(alko, nazwa):
        super().__init__(nazwa, moc=3)


class Wodka(Alkohol):
    """Klasa dla wodki."""

    def __init__(alko, nazwa):
        super().__init__(nazwa, moc=4)


class Bimber(Alkohol):
    """Klasa dla bimbru."""

    def __init__(alko, nazwa):
        super().__init__(nazwa, moc=5)
