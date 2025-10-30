import json
import random
from pathlib import Path

# zakładam poprawność pliku 
def read(paths):
    total = 0
    for path_str in paths:
        path = Path(path_str)
        if path.name != "dane.json" or not path.is_file():
            continue

        with open(path, encoding="utf-8") as f:
            content = json.load(f)

        if content["Model"] == "A":
            total += int(content["Czas"].rstrip("s"))
    return total
