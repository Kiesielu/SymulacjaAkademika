# Symulacja Życia w Akademiku

Prosty, obiektowy symulator w języku Python pokazujący życie studentów w akademiku. Symulacja trwa określony czas (domyślnie 30 dni), w trakcie którego studenci uczą się, odpoczywają, biorą udział w losowych imprezach i piszą kolokwia, co przekłada się na ich statystyki oraz oceny w indeksie.

---

## Jak Uruchomić

### Uruchomienie Symulacji
Aby uruchomić symulację z domyślnymi parametrami (30 dni, losowy seed), wpisz w konsoli:
```bash
python akademik.py
```

Możesz także określić liczbę dni symulacji oraz ziarno generatora losowego (seed) jako parametry:
```bash
python akademik.py [ilosc_dni] [seed]
```

Przykład (symulacja przez 15 dni z seedem "nasz_seed"):
```bash
python akademik.py 15 nasz_seed
```

### Uruchomienie Testów Jednostkowych
Testy zostały napisane przy użyciu biblioteki `pytest`. Aby je uruchomić, wpisz:
```bash
pytest
```
*(lub `.venv/bin/pytest`).*
