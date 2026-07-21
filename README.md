# Programowanie liniowe i optymalizacja

*Zadania z programowania liniowego i optymalizacji — modelowanie i rozwiązywanie problemów LP (studia, PWr).*

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?logo=r&logoColor=white)

## 📖 Opis

Modele programowania liniowego rozwiązywane głównie w Pythonie (PuLP), z jednym równoległym przykładem w R (lpSolve) — od prostych zadań maksymalizacji zysku po problemy transportowe, zagadnienia dualne i programowanie dynamiczne.

## 📂 Struktura

| Folder | Zawartość |
|---|---|
| `lekcja02/` | `zakup_tokenow_trzy_pakiety.py`, `zakup_tokenow_dwa_pakiety.py` — maksymalizacja liczby tokenów kupionych z pakietów przy ograniczonym budżecie; `zakup_tokenow_lpsolve.R` — ten sam problem w R/lpSolve; `minimalizacja_transferow_pieniedzy.py` — minimalizacja liczby/kwoty przelewów rozliczających długi między 4 osobami |
| `lekcja03/` | `optymalizacja_zakupu_pudelek.py` — maksymalizacja wartości zakupionych pudełek przy dwóch wariantach budżetu; `problem_transportowy_max_dochod.py` — klasyczny problem transportowy maksymalizujący dochód; `maksymalizacja_produkcji_tortilli.py` — maksymalizacja produkcji przy ograniczonych składnikach |
| `lekcja04/` | `optymalizacja_garderoby.py` (+ wersja uproszczona) — zysk z kupna/sprzedaży ubrań przy minimach magazynowych; `optymalizacja_produkcji_ciastek.py` — zysk z dwóch receptur ciastek przy ograniczonych składnikach; `dualny_problem_produkcji_ciastek.py` — problem dualny do powyższego (minimalizacja kosztu składników) |
| `lekcja05/` | `problem_transportowy_najtansze_zakupy.py` (+ wersja ogólna) — problem transportowy minimalizujący koszt zakupów 4 studentów w 4 sklepach; `optymalizacja_kosztow_produkcji_energii.py` — minimalizacja miesięcznego kosztu produkcji/magazynowania energii |
| `lekcja06/` | `rozmieszczanie_ksztaltow_na_siatce.py` — rozmieszczanie nienachodzących na siebie figur na siatce 100×100; `najkrotsza_droga_programowanie_dynamiczne.py` — najkrótsza droga w grafie metodą programowania dynamicznego |

## 🛠️ Technologie

| Technologia | Szczegóły |
|---|---|
| Python | PuLP (modelowanie i rozwiązywanie LP) |
| R | lpSolve |

## 👤 Autor

Michał Frąckowiak
