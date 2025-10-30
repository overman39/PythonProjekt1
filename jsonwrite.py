import json
import random
from pathlib import Path

def write(paths):
    for path_str in paths:
        path = Path(path_str)
        path.parent.mkdir(parents=True, exist_ok=True)

        model = random.choice(["A", "B", "C"])
        wynik = random.randint(0, 1000)
        czas = f"{random.randint(0, 1000)}s"

        data = {
            "Model": model,
            "Wynik": wynik,
            "Czas": czas
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)