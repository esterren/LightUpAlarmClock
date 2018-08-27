'''
Setup Script for LUAC
'''

from setuptools import setup, find_packages

setup(name='luac',
      version='0.1',
      description='Light Up Alarm Clock',
      author='Renato Estermann',
      url='https://github.com/esterren/luac',
      packages=find_packages(),
      install_requires=[
        'asciimatics'
      ],)