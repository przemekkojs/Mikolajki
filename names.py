import json
import random

def check_lists(n1:list[str], n2:list[str]) -> bool:
    for i in range(len(n1)):
        name1 = names1[i]
        name2 = names2[i]

        if name1 == name2:
            return False
        
    return True

names1:list[str] = sorted(["Ola Sz.", "Filip", "Artem", "Alan", "Julka", "Gosia", "Ola Ł.", "Przemek", "Wojtek",
                           "Pani Kazia", "Madzia", "Wiktoria", "Bartek", "Mira", "Ida", "Pani Agnieszka"])

names2:list[str] = names1.copy()

names_count:int = len(names1)
file_path:str = "js/names.json"

while not check_lists(names1, names2):
    random.shuffle(names2)

pairs:dict[str, str] = {}

for i in range(names_count):
    pairs[names1[i]] = names2[i]

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(pairs, f, ensure_ascii=False, indent=2)
