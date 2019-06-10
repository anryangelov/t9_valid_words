```
python valid_words_1.py 2283
cate
cave
bate

python valid_words_2.py 2283
bate
cave
cate

It is provided two solutions.

The complexity of the first solution is roughly O(4ⁿ) where n is the number of the given digits.

The complexity of the second solution is roughly O(n*m)
where n is the number of words in the spellchecker dictionary (in our case around 100 000) and m is average length of the words in this dictionary.
However once the spellchecker dictionary is converted to t9 digits finding t9 digits is O(1) - just checking python dictionary.
```