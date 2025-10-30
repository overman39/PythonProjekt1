Zadanie trzecie z Pythona.

Podział zadań.
Maciej Zygmunt -- opracowanie pliku mainscript.py, README.md, jsonread.py;
Piotr Haduch -- tworzenie plików genpaths.py oraz jsonwrite.py.

(1) Użytkownik podaje. 
(1.1) Miesiące pełnymi nazwami (przynajmniej jeden miesiąc).
(1.2) Dni standardowymi skrótami lub przedział dni. (tyle przedziałów, ile miesięcy)
(1.3) Pory dnia r -- rano lub w -- wieczorem. (domyślnie rano; jeśli podał więcej pór niż dni, to daj w genpaths.py błąd)
(1.4) Opcję --wrtite, jeśli chce trworzyć plik. Opcja --read, czyli chce czytać plik.
(1.5) Opcję --root, jeśli chce tworzyć pliki w określonym directory. W przeciwnym razie katalogi tworzymy w obecnym directory.
(1.6) Program przekazuje arguments do genpaths.py. Funkcja generate(arguments) ma przekazać tablicę ścieżek.

(2) Jeśli użytkownik poda niepoprawne nazwy, program ma przekazać błąd.

(3) Program genpaths.py ma z inputu (arguments) stworzyć trzy tablice.
(3.1) Tablicę miesięcy.
(3.2) Tablicę tablic dni w każdym miesiącu.
(3.3) Tablicę pór dla każdego z dni.

(4) Następnie ma, korzystając z tych tablic, przekazać gotowe ścieżki jako stringi.

(5) Program jsonwrite.py ma tworzyć pliki w funkcji write(paths). 
(5.1) Jeśli plik istnieje i użytkownik chce go utworzyć, nadpisujemy.
(5.2) Plik ma być w formie
    {
    "Model": "B",
    "Wynik": 379,
    "Czas": "35s"
    }

(6) Program jsonread.py ma odczytywać pliki w funkcji read(paths).
(6.1) Jeśli nie ma plików do odczytu, nic nie rób, tylko podaj wartość 0 s.
(6.2) Odczytujemy tylko pliki o nazwie dane.json i zakładamy, że taki plik jest poprawnie sformatowany.