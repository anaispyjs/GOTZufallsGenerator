import random
import json
import os
import sys


def load_characters(filename="characters.json"):
    characters = []

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


def get_str_if_unicode(text):
    if sys.version_info[0] == 2 and type(text) == unicode:
        return text.encode("utf-8")


def generate_spoiler(characters, text_blocks):

    assert len(characters) >= 1, "You need to pass at least one character"
    assert len(text_blocks) >= 1, "You need to pass at least one text block"

    charakter = get_str_if_unicode(random.choice(characters))
    charakterzwei = get_str_if_unicode(random.choice(characters))
    textbaustein = get_str_if_unicode(random.choice(text_blocks))

    if len(textbaustein) > 0 and textbaustein[-1] != ".":
        print("{0} {1} {2}.".format(charakter, textbaustein, charakterzwei))
    else:
        print("{0} {1}".format(charakter, textbaustein))

    return generate_spoiler


if __name__ == "__main__":
    generate_spoiler(load_characters(), get_text_blocks())
