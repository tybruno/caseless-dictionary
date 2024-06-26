"""Setup.py"""
from setuptools import (
    find_packages,
    setup,
)

__version__ = 'v2.0.1'
__author__ = 'Tyler Bruno'
DESCRIPTION = (
    'Typed and Tested Case Insensitive Dictionary which was '
    'inspired by Raymond Hettinger'
)
INSTALL_REQUIRES = ('modifiable-items-dictionary >= 3.0.0',)


with open('README.md', 'r', encoding='utf-8') as file:
    README = file.read()

setup(
    name='caseless-dictionary',
    version=__version__,
    author=__author__,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    keywords='python dict dictionary',
    url='https://github.com/tybruno/caseless-dictionary',
    license='MIT',
    package_data={'caseless-dictionary': ['py.typed']},
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: ' 'Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)
