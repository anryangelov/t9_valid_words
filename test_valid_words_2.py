import pytest

from valid_words_2 import make_t9_dictionary


@pytest.fixture(scope='module')
def t9_dictionary():
    return make_t9_dictionary()


@pytest.mark.parametrize(
    'given_digits, expected_words',
    [('1', []),
     ('0', []),
     ('22833', ['acted', 'bated', 'caved']),
     ('2287', ['acts', 'bats', 'baur', 'cats']),
     ('541552423', [])]
)
def test_valid_words(given_digits, expected_words, t9_dictionary):
    got_words = t9_dictionary[given_digits]
    got_words = sorted(got_words)

    assert expected_words == got_words
