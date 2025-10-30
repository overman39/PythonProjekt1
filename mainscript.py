import argparse
from pathlib import Path

# moduł odpowiadający za odczyt plików
import jsonread
# moduł odpowiadający za tworzenie plików
import jsonwrite
# moduł generujący ścieżki z inputu
import genpaths

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description = "Tworzenie i odczyt plików formatu *.json."
    )
    parser.add_argument(
        "--months",
        required = True,
        help = "Podaj listę miesięcy, oddzielając je przecinkami, np. styczeń, luty.",
    )
    parser.add_argument(
        "--days",
        required = True,
        help = "Podaj zakresy dni dla kolejnych miesięcy, oddzielając je przecinkami. Stosuj standardowe skróty: pon, wt, śr, czw, pt, sob, nd.",
    )
    parser.add_argument(
        "--times",
        default="r",
        help = "Podaj pory dnia: r, jeśli rano, w, jeśli wieczorem. Domyślnie ustawiamy na rano.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--write",
        action="store_true",
        help="Utwórz / nadpisz pliki (zapis).",
    )
    group.add_argument(
        "--read",
        action="store_true",
        help="Odczytaj pliki i policz sumę czasów dla modelu A.",
    )
    parser.add_argument(
        "--root",
        default = ".",
        help = "Domyślnie katalog bazowy jest ustawiany na bieżący. Dodaj, jeśli chcesz inny korzeń."
    )

    arguments = parser.parse_args()

    # podajemy args do pliku genpath.py, który wygeneruje odpowiednie ścieżki do pliku
    paths = genpaths.generate(arguments)

    # tworzenie plików
    if arguments.write:
        jsonwrite.write(paths)

    # odczyt plików
    else:
        total = jsonread.read(paths)
        print(f"Suma czasów dla modelu A wynosi {total} s.")

