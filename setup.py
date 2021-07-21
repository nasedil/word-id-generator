# -*- coding: UTF-8 -*-
from setuptools import setup

setup(name='wordidgen',
      packages=['wordidgen'],
      entry_points={
        'console_scripts': ['wordidgen = wordidgen.wordidgen:main']
      })
