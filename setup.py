# -*- coding: UTF-8 -*-
from setuptools import setup

setup(name='wordidgen',
      packages=['wordidgen'],
      version = '0.0.5',
      entry_points={
        'console_scripts': ['wordidgen = wordidgen.wordidgen:main']
      })
