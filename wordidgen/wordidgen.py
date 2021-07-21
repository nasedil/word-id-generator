#!/usr/bin/python
# -*- coding: UTF-8 -*-
from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser

def main():
    """Helper command-line tool for word id generator."""
    parser = ArgumentParser(description='Word id generator',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l', '--len',
                        type=int,
                        help='number of syllables in the word')
    parser.add_argument('-c', '--capitalize',
                        action='store_true',
                        help='whether the word should be capitalized')
    args = parser.parse_args()
    word = 'хо' * args.len
    if args.capitalize:
        word = word.capitalize()
    print(word)

if __name__ == '__main__':
    main()
