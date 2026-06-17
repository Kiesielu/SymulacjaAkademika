class Alkohol:
    def __init__(alko, nazwa, moc):
        alko.nazwa = nazwa
        alko.moc = moc

    def wypij_przez(alko, stud):
        stud.stres -= alko.moc * 2
        stud.spoleczny += alko.moc * 3


class Piwo(Alkohol):
    def __init__(alko, nazwa):
        super().__init__(nazwa, moc=1)


class Wino(Alkohol):
    def __init__(alko, nazwa):
        super().__init__(nazwa, moc=3)


class Wodka(Alkohol):
    def __init__(alko, nazwa):
        super().__init__(nazwa, moc=4)


class Bimber(Alkohol):
    def __init__(alko, nazwa):
        super().__init__(nazwa, moc=5)
