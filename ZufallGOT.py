import random
import json
with open("characters.json") as characterfile:
	characters = json.load(characterfile)
textbausteine = [ 'ist ein Kind von','stirbt.','kriegt bald ein Kind.', 'ist in Wahrheit ein Tagaryen.']


charakter = random.choice(characters)
charakterzwei = random.choice(characters)
textbaustein = random.choice(textbausteine)


if textbaustein[-1] != ".":
    print("{0} {1} {2}.".format(charakter, textbaustein, charakterzwei))
else:
    print("{0} {1}".format(charakter, textbaustein))
    
    