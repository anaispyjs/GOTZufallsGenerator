import json
names = []
with open("characters.txt") as charfile:
    for line in charfile:
        names.append(line.strip())
with open("characters.json", "w") as namefile:
    json.dump(names, namefile)
