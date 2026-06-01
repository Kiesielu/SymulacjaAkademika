from studenci import Kujon, inicjalizuj_gre

#seed zukchrabonscz
inicjalizuj_gre("zukchrabonszcz")
student1 = Kujon("Student1Kujon")
print(
    f"{student1.imie} -> Wiedza: {student1.wiedza}, Stres: {student1.stres}, Towarzyskość: {student1.spoleczny}"
)
#seed <brak>
inicjalizuj_gre(None)
student2 = Kujon("Student2Kujon")
print(
    f"{student2.imie} -> Wiedza: {student2.wiedza}, Stres: {student2.stres}, Towarzyskość: {student2.spoleczny}"
)