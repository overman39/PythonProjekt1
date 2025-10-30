from pathlib import Path
import os

# pełne nazwy miesięcy
MONTHS = [
    "styczeń",
    "luty",
    "marzec",
    "kwiecień",
    "maj",
    "czerwiec",
    "lipiec",
    "sierpień",
    "wrzesień",
    "październik",
    "listopad",
    "grudzień",
]

# pełne nazwy dni tygodnia
DAYS = [
    "poniedziałek",
    "wtorek",
    "środa",
    "czwartek",
    "piątek",
    "sobota",
    "niedziela",
]

# skróty --> pełne nazwy dni
DAY_MAP = {
    "pon": "poniedziałek",
    "wt": "wtorek",
    "śr": "środa",
    "czw": "czwartek",
    "pt": "piątek",
    "sob": "sobota",
    "nd": "niedziela",
}

# skróty --> pełne nazwy pór dnia
TIME_MAP = {
    "r": "rano",
    "w": "wieczorem",
}

# sporządzamy listę miesięcy
def months_list(string):
    if not string.strip():
        raise ValueError("Nie podano żadnych miesięcy.")
    months = [x.strip().lower() for x in string.split(",")]

    # sprawdza poprawność argumentów
    for m in months:
        if m not in MONTHS:
            raise ValueError(f"Nieznany miesiąc: '{m}'")
    return months

# rozszerza zapis np. "pon - śr" --> ["poniedziałek", "wtorek", "środa"]
def day_range(string):
    string = string.strip().lower()

    if not string:
        return []

    # jeśli podano tylko dzień tygodnia
    if "-" not in string:
        if string not in DAY_MAP:
            raise ValueError(f"Nieznany skrót dnia: '{string}'")
        return [DAY_MAP[string]]
    
    # jeśli podano zakres
    start, end = [x.strip() for x in string.split("-", 1)]
    if start not in DAY_MAP or end not in DAY_MAP:
        raise ValueError(f"Niepoprawny zakres dni: '{string}'")
    start_name, end_name = DAY_MAP[start], DAY_MAP[end]
    start_index, end_index = DAYS.index(start_name), DAYS.index(end_name)
    result = []
    current = start_index
    while current != end_index:
        result.append(DAYS[current])
        current = (current + 1) % 7
    result.append(DAYS[end_index])
    return result

# przetwarza dni dla każdego miesiąca
def days_list(string, num_months):
    arguments = [x.strip() for x in string.split(",")]
    if len(arguments) != num_months:
        raise ValueError(
            f"Podano niepoprawną liczbę zakresów dni."
        )
    result = []
    for arg in arguments:
        result.append(day_range(arg))
    return result


# tworzy listę pór dnia
def times_list(argument, num_days):
    args = [x.strip() for x in argument.split(",")]
    result = []
    for arg in args:
        name = arg.strip().lower()
        if name not in TIME_MAP:
            raise ValueError(f"Nieznana pora dnia: '{arg}'")
        result.append(TIME_MAP[name])
    # jak za dużo, to błąd
    if len(result) > num_days:
        raise ValueError(f"Zbyt długa lista pór: '{len(result)}'")
    # dopisz ranki :)
    result.extend(["rano"] * (num_days - len(result)))
    return result


# tworzy pełne ścieżki
def path_generator(months, days, times, root):
    paths = []
    current_day = 0
    for month_index, month in enumerate(months):
        for day in days[month_index]:
            time = times[current_day]
            current_day += 1
            dirpath = root / month / day / time
            dirpath.mkdir(parents=True, exist_ok=True)
            paths.append(dirpath / "dane.json")
    return paths

# główna funkcja wywoływana przez main.py
def generate(arguments):
    months = months_list(arguments.months)
    days = days_list(arguments.days, len(months))
    num_days = sum(len(d) for d in days)
    times = times_list(arguments.times, num_days)
    root = Path(arguments.root).resolve()
    return path_generator(months, days, times, root)