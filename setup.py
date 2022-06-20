""" setup.py for package """
from setuptools import setup

with open('requirements.txt', 'r') as requirements_file:
    requirements = requirements_file.readlines()

if __name__ == '__main__':
  setup(
   install_requires=requirements,
  )
