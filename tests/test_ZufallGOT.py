from hypothesis import given, reject, example
from hypothesis.strategies import text, lists, sampled_from
from ZufallGOT import load_characters, generate_spoiler, get_str_if_unicode, \
                        get_text_blocks
import glob


@given(sampled_from(glob.glob("data/*") + ['']))
def test_load_characters(filename):
    try:
        characters = load_characters(filename)
        assert isinstance(characters, list)
    except IOError:
        reject()


@given(lists(text()), lists(text()))
@example(get_text_blocks(), load_characters())
def test_generate_spoiler(characters, text_blocks):
    try:
        spoiler = generate_spoiler(characters, text_blocks)
    except AssertionError:
        reject()


@given(text())
def test_get_str_if_unicode(text):
    res = get_str_if_unicode(text)
    assert isinstance(res, str)
