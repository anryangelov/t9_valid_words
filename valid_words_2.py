import string
import sys
from collections import defaultdict

from spellchecker import SpellChecker


letters = string.ascii_lowercase
t9_digits = '22233344455566677778889999'
t9map = dict(zip(letters, t9_digits))


def translate_dictionary_into_t9_digits(dictionary):
    word_digits = {}

    for word in dictionary:
        in_digits = []

        if not word.isalpha():
            continue

        for letter in word:
            digit = t9map[letter]
            in_digits.append(digit)

        word_digits[word] = ''.join(in_digits)

    return word_digits


def make_t9_dictionary():
    spell = SpellChecker()
    dictionary = spell.word_frequency.dictionary

    word_digits = translate_dictionary_into_t9_digits(dictionary)

    digits_words = defaultdict(set)

    for word, digits in word_digits.items():
        digits_words[digits].add(word)

    return digits_words


if __name__ == '__main__':
    digits = sys.argv[1]

    digits_words = make_t9_dictionary()

    words = digits_words[digits]

    for word in words:
        print(word)
