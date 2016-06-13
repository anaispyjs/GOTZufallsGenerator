from hypothesis import given, reject, example
from hypothesis.strategies import text, lists
from ZufallGOT import load_characters, generate_spoiler


@given(text())
@example("characters.json")
@example("characters.py")
@example("characters.txt")
def test_load_characters(filename):
    characters = load_characters(filename)
    assert isinstance(characters, list)


@given(lists(text()), lists(text()))
def test_generate_spoiler(characters, filenames):
    try:
        spoiler = generate_spoiler(characters, filenames)
    except AssertionError:
        reject()
