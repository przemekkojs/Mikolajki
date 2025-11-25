import json
import random

names1:list[str] = sorted(["Ola Sz.", "Filip", "Artem", "Alan", "Julka", "Gosia", "Ola Ł.", "Przemek", "Wojtek",
                           "Pani Kazia", "Madzia", "Wiktoria", "Bartek", "Mira", "Ida", "Pani Agnieszka"])

names2:list[str] = names1.copy()

is_bad:bool = True
names_count:int = len(names1)
file_path:str = "js/names.json"

while is_bad:
    is_bad = False
    
    for i in range(names_count):
        name1 = names1[i]
        name2 = names2[i]

        if name1 == name2:
            is_bad = True
            break

    random.shuffle(names2)

pairs:dict[str, str] = {}

for i in range(names_count):
    pairs[names1[i]] = names2[i]

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(pairs, f, ensure_ascii=False, indent=2)
