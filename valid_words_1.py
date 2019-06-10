from itertools import product
import sys

from spellchecker import SpellChecker


t9 = ('', '', 'abc', 'def', 'cgh', 'jkm', 'mno', 'pqrs', 'tuv', 'wxyz')


def get_valid_words(digits):
    t9_letters = [t9[int(digit)] for digit in digits if int(digit) > 1]

    t9_words = product(*t9_letters)  # all possible combination
    t9_words = [''.join(word) for word in t9_words]

    spell = SpellChecker()
    valid_words = spell.known(t9_words)

    return valid_words


if __name__ == '__main__':
    digits = sys.argv[1]
    words = get_valid_words(digits)
    for word in words:
        print(word)
