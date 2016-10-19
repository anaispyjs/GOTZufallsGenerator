import json


names = []
with open("data/characters.txt") as charfile:
    for line in charfile:
        names.append(line.strip())
with open("data/characters.json", "w") as namefile:
    json.dump(names, namefile)
