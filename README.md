# Symulacja Życia w Akademiku

Symulator w języku Python pokazujący życie studentów w akademiku. Symulacja trwa określony czas (domyślnie 30 dni), w trakcie którego studenci uczą się, odpoczywają, biorą udział w losowych imprezach i piszą kolokwia, co przekłada się na ich statystyki oraz oceny w indeksie.

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

TBA

Klasa `Student` automatycznie dba o to, by atrybuty nie wykroczyły poza zakres `0-100`.

### 3. `indeks.py`
Klasa `Indeks` symuluje fizyczny indeks studenta. Przechowuje listę ocen oraz wylicza średnią ocen.

### 4. `alkohole.py`
Klasa bazowa `Alkohol` oraz jej podklasy (`Piwo`, `Wino`, `Wodka`, `Bimber`). Każdy alkohol posiada swoją "moc" (w skali 1-5). Wypicie alkoholu przez studenta obniża jego stres i podnosi towarzyskość proporcjonalnie do mocy napoju.

### 5. `wydarzenia.py`
Definiuje losowe zdarzenia, które mogą przydarzyć się studentom w akademiku:
*   `LosowaImpreza` – studenci piją losowo wybrany alkohol (Piwo, Wino, Wódka, Bimber). Obniża to ich wiedzę, ale też zmniejsza stres i poprawia statystyki towarzyskie.
*   `LosoweKolokwium` – studenci piszą sprawdzian, co generuje stres (+35). Jeśli stres wynosi 80 lub więcej, istnieje 50% szans, że student zaśpi na kolokwium, co skutkuje automatycznym otrzymaniem oceny `2`. W przeciwnym razie, w zależności od poziomu wiedzy, otrzymuje:

Do kalibracji!!
    
*   `Mechanika Ściągania` - Jeśli ocena studenta wynosi poniżej `5`, a jego towarzyskość (`spoleczny`) wynosi przynajmniej `50`, spróbuje on ściągać od innego obecnego studenta z wiedzą >= 40. Istnieje **70% szans na sukces** (ocena wzrasta do **4**) oraz **30% szans na przyłapanie** (ocena spada do **2**).

### 6. `silnik.py`
Klasa `SilnikSymulacji` kontroluje przebieg każdego dnia:
1.  Wylosowanie głównej aktywności na dany dzień: nauka lub odpoczynek.
2.  Wykonanie odpowiednich akcji dla każdego studenta w ekipie.
3.  Z szansą 50% wylosowanie i uruchomienie zdarzenia specjalnego (`LosowaImpreza` lub `LosoweKolokwium`).
4.  Wypisanie raportu ze stanem statystyk studentów na koniec dnia.

---

## Jak Uruchomić

### Uruchomienie Symulacji
Aby uruchomić symulację z domyślnymi parametrami (30 dni, losowy seed), wpisz w konsoli:
```bash
python akademik.py
```

Można także określić liczbę dni symulacji oraz seed jako parametry:
```bash
python akademik.py [ilosc_dni] [seed]
```
