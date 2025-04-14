from pathlib import Path

from pyUtils import ConfigFileManager
from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    longDescription: str = f.read()
configFilePath: str = Path(__file__).parent / 'dist' / 'config' / 'config.toml'
config = ConfigFileManager(configFilePath)
with open('requirements.txt') as f:
    requirements: list = [line.replace('\n', '')
                          for line in f.readlines()
                          if line != '\n']


setup(
    name= config.app.namem,
    version= config.app.version,
    description= 'Home assistant project with learning purposes.',
    long_description= longDescription,
    long_description_content_type= 'text/markdown',
    author= 'Jaimead7',
    author_email= 'alvarez.diaz.jaime1@gmail.com',
    url= 'https://github.com/Jaimead7/HomeAssistant',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    license= 'MIT',
    install_requires= requirements,
    python_requires= '>=3.13',
)
