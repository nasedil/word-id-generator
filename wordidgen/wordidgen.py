#!/usr/bin/python
# -*- coding: UTF-8 -*-
from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser

import random

class WordGenerator:
    """Generate word by combining syllables"""

    def __init__(self,
                 consonants='бвгджзклмнпрстфхцчшщ',
                 vowels='аяоёуюэеыи',
                 length=4):
        self.consonants = consonants
        self.vowels = vowels
        self.length = length
        self.syllable_count = len(self.consonants) * len(self.vowels)
        self.count = self.syllable_count ** self.length

    def generate(self, capitalize=False, number=None):
        """Generate a word"""
        word = ''
        if number is None:
            number = random.randrange(self.count)
        for i in range(self.length):
            r = number % self.syllable_count
            number = number // self.syllable_count
            c_index = r // len(self.vowels)
            v_index = r % len(self.vowels)
            word += self.consonants[c_index] + self.vowels[v_index]
            print(number, word, r, c_index, v_index)
        if capitalize:
            word = word.capitalize()
        return word

def main():
    """Helper command-line tool for word id generator."""
    parser = ArgumentParser(description='Word id generator',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l', '--length',
                        type=int,
                        default=4,
                        help='number of syllables in the word')
    parser.add_argument('-n', '--number',
                        type=int,
                        default=-1,
                        help='number of the word (random otherwise)')
    parser.add_argument('-t', '--title',
                        action='store_true',
                        help='whether the word should be capitalized')
    parser.add_argument('-c', '--count',
                        action='store_true',
                        help='print number of possible words')
    args = parser.parse_args()
    worg_generator = WordGenerator(length=args.length)
    if args.count:
        print(worg_generator.count)
        return
    word = worg_generator.generate(capitalize=args.title)
    print(word)

if __name__ == '__main__':
    main()
