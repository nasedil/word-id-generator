#!/usr/bin/python
# -*- coding: UTF-8 -*-
from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser

def main():
    """Helper command-line tool for word id generator."""
    parser = ArgumentParser(description='Word id generators',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()
    print('Хыхо')

if __name__ == '__main__':
    main()
