# -*- coding: UTF-8 -*-

import locale
locale.setlocale(locale.LC_ALL, "")

import pytest

from wordidgen import wordidgen

def test_wordidgen():
    word_generator = wordidgen.WordGenerator(length=1)
    words = []
    for i in range(word_generator.count):
        words.append(word_generator.generate(number=i))
    assert words == sorted(words, key=locale.strxfrm)
    assert word_generator.count == 185
    word_generator = wordidgen.WordGenerator(length=2)
    assert word_generator.generate(number=0) == 'баба'
    assert word_generator.generate(number=185) == 'беба'
    assert word_generator.generate(number=187) == 'бебё'