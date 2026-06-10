# Symulacja Życia w Akademiku

Obiektowy symulator w języku Python pokazujący życie studentów. Symulacja trwa określony czas (domyślnie 30 dni), w trakcie którego studenci uczą się, odpoczywają, biorą udział w losowych imprezach i piszą kolokwia, co przekłada się na ich statystyki oraz oceny w indeksie.

## Główne Statystyki Studenta
Każdy student posiada trzy kluczowe atrybuty, które są automatycznie ograniczane do przedziału [0, 100]:
*   **Wiedza** (`wiedza`) – wzrasta podczas nauki, maleje podczas imprez. Wpływa na oceny z kolokwiów.
*   **Stres** (`stres`) – wzrasta podczas nauki i kolokwiów, maleje pod wpływem alkoholu.
*   **Towarzyskość** (`spoleczny`) – statystyka społeczna, zmienia się w zależności od typu studenta i spożywanych trunków.

---

## Architektura i Struktura Plików

### 1. `akademik.py`
Punkt wejściowy programu. Odpowiada za zainicjalizowanie generatora liczb losowych oraz uruchomienie silnika symulacji na 30 dni.

### 2. `studenci.py`
Zawiera definicję klasy bazowej `Student` oraz jej wyspecjalizowanych podklas:
*   `Kujon` – uczy się najefektywniej (+20 wiedzy), ale kosztuje go to sporo stresu (+10) i traci na towarzyskości (-5).
*   `Imprezowicz` – nauka przychodzi mu ciężko (+2 wiedzy, +2 stresu), ale zyskuje ogromne punkty towarzyskie (+15).
*   `Tancerz` – uczy się umiarkowanie (+5 wiedzy, +1 stresu) i zyskuje towarzyskość (+10).
*   `Gawendziarz` – standardowy profil studenta (dziedziczy domyślne tempo nauki: +10 wiedzy, +5 stresu, +5 towarzyskości).

Klasa `Student` automatycznie dba o to, by atrybuty nie wykroczyły poza zakres `0-100`.

### 3. `indeks.py`
Klasa `Indeks` symuluje fizyczny indeks studenta. Przechowuje listę ocen oraz udostępnia metodę `pokaz_srednia()` wyliczającą średnią ocen (zwraca `0.0`, jeśli brak ocen).

### 4. `alkohole.py`
Klasa bazowa `Alkohol` oraz jej podklasy (`Piwo`, `Wino`, `Wodka`, `Bimber`). Każdy alkohol posiada swoją "moc" (w skali 1-5). Wypicie alkoholu przez studenta (`wypij_przez(stud)`) obniża jego stres i podnosi towarzyskość proporcjonalnie do mocy napoju.

### 5. `wydarzenia.py`
Definiuje losowe zdarzenia, które mogą przydarzyć się studentom w akademiku:
*   `LosowaImpreza` – studenci piją losowo wybrany alkohol (Piwo, Wino, Wódka, Bimber). Obniża to ich wiedzę, ale też zmniejsza stres i poprawia statystyki towarzyskie.
*   `LosoweKolokwium` – studenci piszą sprawdzian, co generuje stres (+35). W zależności od aktualnego poziomu wiedzy, student otrzymuje do indeksu ocenę:
    *   `5` (wiedza >= 40)
    *   `3` (wiedza >= 20)
    *   `2` (wiedza < 20)

### 6. `silnik.py`
Klasa `SilnikSymulacji` kontroluje przebieg każdego dnia:
1.  Wylosowanie głównej aktywności na dany dzień: **nauka** lub **odpoczynek**.
2.  Wykonanie odpowiednich akcji dla każdego studenta w ekipie.
3.  Z szansą 50% wylosowanie i uruchomienie zdarzenia specjalnego (`LosowaImpreza` lub `LosoweKolokwium`).
4.  Wypisanie raportu ze stanem statystyk studentów na koniec dnia.

---

## Jak Uruchomić

### Uruchomienie Symulacji
Aby uruchomić symulację, wpisz w konsoli:
```bash
python akademik.py
```
*(lub `.venv/bin/python akademik.py` w przypadku korzystania ze środowiska wirtualnego).*

### Uruchomienie Testów Jednostkowych
Testy zostały napisane przy użyciu biblioteki `pytest`. Aby je uruchomić, wpisz:
```bash
pytest
```
*(lub `.venv/bin/pytest`).*
