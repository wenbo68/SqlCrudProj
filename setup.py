from setuptools import setup, find_packages
from typing import List

Hyphen_e = '-e .'

def get_requirement(filename: str) -> List[str]:
    requirements = []
    with open(filename) as obj:
        requirements = obj.readlines()
        requirements = [req.replace('/n','') for req in requirements]

        if Hyphen_e in requirements:
            requirements.remove(Hyphen_e)
    return requirements

setup(
    name = 'mongodb_connect',
    version = '0.1.0',
    author='Wenbo',
    author_email='wenboliu68@gmail.com',
    install_requires = get_requirement('requirements.txt')
    package_dir={"":"src"},
    packages=find_packages(where='src')
)