import random
import json
def load_characters(filename = "characters.json"):
	with open(filename) as characterfile:
		characters = json.load(characterfile)
	return characters


def get_text_blocks():
	text_blocks = [ 'ist ein Kind von','stirbt.','kriegt bald ein Kind.', 'ist in Wahrheit ein Tagaryen.']
	return text_blocks


def generate_spoiler(characters, text_blocks):
	charakter = random.choice(characters)
	charakterzwei = random.choice(characters)
	textbaustein = random.choice(text_blocks)

	if textbaustein[-1] != ".":
	    print("{0} {1} {2}.".format(charakter, textbaustein, charakterzwei))
	else:
	    print("{0} {1}".format(charakter, textbaustein))

	return generate_spoiler


if __name__ == "__main__":
	generate_spoiler(load_characters(), get_text_blocks())