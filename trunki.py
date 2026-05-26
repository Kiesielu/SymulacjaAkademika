class trunki:
    def __init__(alko, nazwa: str, moc: int) -> None:
        alko.nazwa: str = nazwa
        alko.moc: int = moc #skala 1-5

    def wypij_przez(alko, stud) -> None:
        stud.stres -= alko.moc * 2
        stud.spoleczny += alko.moc * 3

class Piwo(Alkohol):
    def __init__(alko, nazwa: str) -> None:
        super().__init__(nazwa, moc=1)

class Wino(Alkohol):
    def __init__(alko, nazwa: str) -> None:
        super().__init__(nazwa, moc=3)

class Wodka(Alkohol):
    def __init__(alko, nazwa: str) -> None:
        super().__init__(nazwa, moc=4)

class Bimber(Alkohol):
    def __init__(alko, nazwa: str) -> None:
        super().__init__(nazwa, moc=5)