#!/usr/bin/python
# -*- coding: UTF-8 -*-
from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser
from collections import namedtuple
import os
import random

CONFIG_FOLDER = 'wordidgen-a20ad162-f2cb-11eb-81a6-33a7c6316f2d'

Consonant = namedtuple('Consonant', ['hard_letter', 'soft_letter'])
Vowel = namedtuple('Vowel', ['letter', 'is_soft'])

CONSONANTS_REGULAR = [Consonant(l, l) for l in 'бвгджзклмнпрсфхчц']
CONSONANT_T = Consonant('т', None)
CONSONANT_SH = Consonant('ш', 'щ')
CONSONANTS = CONSONANTS_REGULAR + [CONSONANT_T, CONSONANT_SH]

VOWELS_HARD = [Vowel(l, False) for l in 'аоуыэ']
VOWELS_SOFT = [Vowel(l, True) for l in 'яёюие']
VOWELS = VOWELS_HARD + VOWELS_SOFT

class WordGenerator:
    """Generate word by combining syllables"""

    def __init__(self,
                 consonants=CONSONANTS,
                 vowels=VOWELS,
                 length=4):
        self.consonants = consonants
        self.vowels = vowels
        self.length = length
        self.syllables = []
        for i in self.consonants:
            for j in self.vowels:
                if j.is_soft and i.soft_letter is not None:
                    self.syllables.append(i.soft_letter + j.letter)
                if not j.is_soft and i.hard_letter is not None:
                    self.syllables.append(i.hard_letter + j.letter)
        self.syllable_count = len(self.syllables)
        self.count = self.syllable_count ** self.length

    def generate(self, number=None):
        """Generate a word"""
        word = ''
        if number is None:
            number = random.randrange(self.count)
        for i in range(self.length):
            r = number % self.syllable_count
            number = number // self.syllable_count
            word += self.syllables[r]
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
    parser.add_argument('-s', '--save',
                        action='store_true',
                        help='remember that the word was generated')
    parser.add_argument('-u', '--unique',
                        action='store_true',
                        help='do not generate remembered words again')
    args = parser.parse_args()
    word_generator = WordGenerator(length=args.length)
    config_name = 'ба' + str(args.length) + '.txt'
    config_path = os.path.join(os.path.expanduser("~"), '.config',
                               CONFIG_FOLDER, config_name)
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    generated_words = []
    if args.save:
        try:
            with open(config_path, 'rt+') as f:
                generated_words = f.read().splitlines()
        except:
            pass
    if args.count:
        print(word_generator.count)
        return
    if len(generated_words) >= word_generator.count:
        print('All possible unique words are already generated')
        return
    while True:
        #TODO what if all words are already generated?
        #TODO when particular number is needed
        word = word_generator.generate()
        if word not in generated_words:
            break
        print(word, 'duplicate')
    if args.save:
        #TODO need to make thread-safe
        #TODO use correct path on different systems
        with open(config_path, 'at+') as f:
            f.write(word + '\n')
    if args.title:
        word = word.capitalize()
    print(word)

if __name__ == '__main__':
    main()
