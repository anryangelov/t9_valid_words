import pytest

from valid_words_1 import get_valid_words


@pytest.mark.parametrize(
    'given_digits, expected_words',
    [('1', []),
     ('0', []),
     ('22833', ['acted', 'bated', 'caved']),
     ('2287', ['acts', 'bats', 'baur', 'cats']),
     ('541552423', [])]
)
def test_valid_words(given_digits, expected_words):
    got_words = get_valid_words(given_digits)
    got_words = sorted(got_words)

    assert expected_words == got_words
