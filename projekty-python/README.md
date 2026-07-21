# Projekty Python

*Wczesne materiały ze studiów — podstawy Pythona i C++ (semestr 1) oraz projekt zaliczeniowy z kryptografii (semestr 2).*

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?logo=cplusplus&logoColor=white)

## 📖 Opis

Zbiór ćwiczeń z pierwszych dwóch semestrów studiów: podstawy programowania w Pythonie i C++ (semestr 1) oraz większy projekt zaliczeniowy — implementacja funkcji skrótu MD4 i szyfrowania RSA z interfejsem graficznym PyQt5 (semestr 2).

## 📂 Struktura

| Folder | Zawartość |
|---|---|
| `studia/semestr_1/python/lab/alfa/` | Drobne skrypty wprowadzające: generator Fibonacciego (iteracyjny i tablicowy), eksperymenty z krotkami/`math`, wywołania `os.system`, demo zmiennoprzecinkowe |
| `studia/semestr_1/python/sudoku.py/` | Dwa niezależne solvery Sudoku: przez backtracking z użyciem numpy oraz wersja rekurencyjna |
| `studia/semestr_1/python/wyklady/` | Notatki i demonstracje z wykładów: klasy i atrybuty (OOP), operacje na tekstach |
| `studia/semestr_1/Testy_cpp-master/` | Ćwiczenia w C++/Python równoległe do repo [`Algorytmy`](https://github.com/MichalF-lab/Algorytmy): szyfr Cezara, obsługa plików (liczby pierwsze, palindromy, sumy cyfr), struktury (biblioteka książek, wypożyczalnia), klasy statyczne, wskaźniki |
| `studia/semestr_2/programowanie/projekt/` | Projekt zaliczeniowy: implementacja MD4 + RSA + GUI (PyQt5). Finalna, działająca aplikacja to `md4_rsa_gui_aplikacja.py` (`RSA.py`, `MD4.py`, `interface_graficzny.py`) — obok niej zachowane są kolejne warianty/szkice MD4 powstałe po drodze (funkcyjne, klasowe, niedokończone), świadomie nazwane tak, by było widać etapy dochodzenia do finalnej wersji |
| `studia/semestr_2/programowanie/testy/` | `testy.py` — testy jednostkowe finalnej implementacji; `md4_test_odczyt_pliku.py` — ręczny test liczenia hasha pliku |
| `studia/semestr_2/topologia/` | `menu_zadan_tablicowych.cpp` — menu z zadaniami na tablicach (min/max, zliczanie podciągów, duplikaty); `metryka.py` — zadanie z metryk |

## 🛠️ Technologie

| Technologia | Szczegóły |
|---|---|
| Python | PyQt5 (GUI), numpy |
| C++ | podstawowe programowanie proceduralne i strukturalne |

## ⚠️ Uwagi

- Kilka plików (`main_pusty_nieuzywany.py`, `lekcje1_pusty_nieuzywany.py`, `wyklad_pusty_nieuzywany.py`, `tempCodeRunnerFile_autogenerowany_nieuzywany.*`) to puste lub automatycznie wygenerowane pliki (VS Code Code Runner) — zachowane, ale nazwa jasno wskazuje, że nic nie zawierają.
- W `projekt/` obok finalnej aplikacji celowo zostawione są wcześniejsze warianty implementacji MD4 — pokazują iteracyjny proces dochodzenia do działającego rozwiązania, a nie przypadkowe duplikaty.

## 👤 Autor

Michał Frąckowiak
