import random
import json
import os


def load_characters(filename="characters.json"):
    isfile = False
    try:
        isfile = os.path.isfile(filename)
    except ValueError:
        pass

    characters = []

    if isfile:
        with open(filename) as characterfile:
            try:
                characters = json.load(characterfile)
            except ValueError:
                pass

    return characters


def get_text_blocks():
    text_blocks = ['ist ein Kind von',
                   'stirbt.',
                   'kriegt bald ein Kind.',
                   'ist in Wahrheit ein Tagaryen.']
    return text_blocks


def generate_spoiler(characters, text_blocks):

    assert len(characters) >= 1, "You need to pass at least one character"
    assert len(text_blocks) >= 1, "You need to pass at least one text block"

    charakter = random.choice(characters)
    charakterzwei = random.choice(characters)
    textbaustein = random.choice(text_blocks)

    if len(textbaustein) > 0 and textbaustein[-1] != ".":
        print("{0} {1} {2}.".format(charakter, textbaustein, charakterzwei))
    else:
        print("{0} {1}".format(charakter, textbaustein))

    return generate_spoiler


if __name__ == "__main__":
    generate_spoiler(load_characters(), get_text_blocks())
