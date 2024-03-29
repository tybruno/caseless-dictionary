[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/tybruno/caseless-dictionary/branch/main/graph/badge.svg?token=ZO94EJFI3G)](https://codecov.io/gh/tybruno/caseless-dictionary)
# caseless-dictionary

A simple, fast, typed, and tested implementation for a python3.6+ case-insensitive dictionary. This class extends and
maintains the original functionality of the builtin `dict`.

#### Key Features:

* **Easy**: If you don't care about the case of the key in a dictionary then this implementation is easy to use since it
  acts just like a `dict` obj.
* **Great Developer Experience**: Being fully typed makes it great for editor support.
* **Fully Tested**: Our test suit fully tests the functionality to ensure that `CaselessDict` runs as expected.
* **There is More!!!**:
    * [ModifiableItemsDict](https://github.com/tybruno/modifiable-items-dictionary): CaselessDict is built on top of
      the `ModifiableItemsDict`, which is a library that enables the user to modify the key or/and value of `dict` type
      object at runtime.

## Installation

`pip install caseless-dictionary`

## Simple CaselessDict Example

```python
from caseless_dictionary import CaselessDict

normal_dict: dict = {"   CamelCase   ": 1, "  UPPER   ": "TWO", 3: "  Number as Key  "}

caseless_dict: CaselessDict = CaselessDict(normal_dict)

print(caseless_dict)  # {'camelcase': 1, 'upper': 'TWO', 3: 'Number as Key'}

print("CamelCase" in caseless_dict)  # True
print("camelcase" in caseless_dict)  # True

print(caseless_dict[" camelCASE  "])  # 1
```

## Simple UpperCaselessDict Example

```python
from caseless_dictionary import UpperCaselessDict
from typing import Iterable

iterable: Iterable = [("   wArNIng", 0), ("deBug   ", 10)]
upper_caseless_dict: dict = UpperCaselessDict(iterable)
print(upper_caseless_dict)  # {'WARNING': 0, 'DEBUG': 10}

print("warning" in upper_caseless_dict)  # True

upper_caseless_dict["WarninG"] = 30
print(upper_caseless_dict)  # {'WARNING': 30, 'DEBUG': 10}
```

## Simple TitleCaselessDict Example

```python
from caseless_dictionary import TitleCaselessDict
from typing import Iterable

iterable: Iterable = {" Brave   ": 1, "   ProtonMail    ": 2}
title_caseless_dict: dict = TitleCaselessDict(iterable)
print(title_caseless_dict)  # {'Brave': 1, 'Protonmail': 2}

title_caseless_dict.pop("  protonMAIL  ")

print(title_caseless_dict)  # {'Brave': 1}
```

## Acknowledgments

During the class '(Advanced) Python For Engineers III' taught by [Raymond Hettinger](https://github.com/rhettinger),
Raymond taught us how to inherit from the builtin Python `dict` by creating a Case-insensitive Dict.
I thought this was a wonderful learning experience so I decided to create a project that would build upon what he
taught.