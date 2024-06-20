[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Code Style: Blue](https://img.shields.io/badge/code%20style-blue-0000ff.svg)](https://github.com/psf/blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/tybruno/caseless-dictionary/branch/main/graph/badge.svg?token=ZO94EJFI3G)](https://codecov.io/gh/tybruno/caseless-dictionary)
[![Pylint](https://img.shields.io/badge/Pylint-10.0%2F10-green)](10.0/10)
[![Mypy](https://img.shields.io/badge/Mypy-checked-blue)](10.0/10)

# caseless-dictionary

A simple, fast, typed, and tested implementation for a python3.6+ case-insensitive and attribute case-insensitive 
dictionaries. This class extends and maintains the original functionality of the builtin `dict` while providing extra 
features.

#### Key Features:

* **Easy**: If you don't care about the case of the key in a dictionary then this implementation is easy to use since it
  acts just like a `dict` obj. 
* **Attribute Access**: `CaselessAttrDict` allows attribute-style access to dictionary items, providing an alternative, 
  often more readable way to access dictionary items.
* **Great Developer Experience**: Being fully typed makes it great for editor support.
* **Fully Tested**: Our test suit fully tests the functionality to ensure that `CaselessDict` runs as expected.
* **There is More!!!**:
    * [ModifiableItemsDict](https://github.com/tybruno/modifiable-items-dictionary): CaselessDict is built on top of
      the `ModifiableItemsDict`, which is a library that enables the user to modify the key or/and value of `dict` type
      object at runtime.

## Installation

`pip install caseless-dictionary`

## Caseless Dictionaries

| Class Name           | Description                                                    | Example                                                                      |
|----------------------|----------------------------------------------------------------|------------------------------------------------------------------------------|
| CaselessDict         | A dictionary where keys that are strings are case-folded.      | `CaselessDict({"  HeLLO WoRLD  ": 1})  # Output: {'hello world': 1}`         |
| CaseFoldCaselessDict | A dictionary where keys that are strings are case-folded.      | `CaseFoldCaselessDict({"  HeLLO WoRLD  ": 1})  # Output: {'hello world': 1}` |
| LowerCaselessDict    | A dictionary where keys that are strings are in lower case.    | `LowerCaselessDict({"  HeLLO WoRLD  ": 1})  # Output: {'hello world': 1}`    |
| UpperCaselessDict    | A dictionary where keys that are strings are in upper case.    | `UpperCaselessDict({"  HeLLO WoRLD  ": 1})  # Output: {'HELLO WORLD': 1}`    |
| TitleCaselessDict    | A dictionary where keys that are strings are in title case.    | `TitleCaselessDict({"  HeLLO WoRLD  ": 1})  # Output: {'Hello World': 1}`    |
| SnakeCaselessDict    | A dictionary where keys that are strings are in snake case.    | `SnakeCaselessDict({"  HeLLO WoRLD  ": 1})  # Output: {'hello_world': 1}`    |
| KebabCaselessDict    | A dictionary where keys that are strings are in kebab case.    | `KebabCaselessDict({"  HeLLO WoRLD  ": 1})  # Output: {'hello-world': 1}`    |
| ConstantCaselessDict | A dictionary where keys that are strings are in constant case. | `ConstantCaselessDict({"  HeLLO WoRLD  ": 1})  # Output: {'HELLO_WORLD': 1}` |
## Caseless Attribute Dictionaries

| Class Name               | Description                                                                                                 | Example                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| SnakeCaselessAttrDict    | A dictionary where keys that are strings are in snake case and can be accessed using attribute notation.    | `SnakeCaselessAttrDict({"  HeLLO WoRLD  ": 1}).hello_world  # Output: 1`    |
| ConstantCaselessAttrDict | A dictionary where keys that are strings are in constant case and can be accessed using attribute notation. | `ConstantCaselessAttrDict({"  HeLLO WoRLD  ": 1}).HELLO_WORLD  # Output: 1` |

### Basic CaselessDict Example

```python
from caseless_dictionary import CaselessDict

# Create a CaselessDict
caseless_dict = CaselessDict({"  HeLLO WoRLD  ": 1, 2: "two"})

print(caseless_dict)  # Output: {'hello world': 1, 2: 'two'}

# Accessing the value using different cases
print(caseless_dict["  hello world  "])  # Output: 1
print(caseless_dict["  HELLO WORLD  "])  # Output: 1

# Accessing non string value
print(caseless_dict[2])  # Output: two
```

### Caseless Dictionary with Key as Str Only

```python
from caseless_dictionary import CaselessDict

# Create a CaselessDict with key_is_str_only set to True
CaselessDict.key_is_str_only = True
caseless_dict = CaselessDict({"  HeLLO WoRLD  ": 1})

# Attempt to set a non-string key
try:
    caseless_dict[1] = 2
except TypeError:
    print("TypeError raised as expected when key_is_str_only is True")
```


### Basic SnakeCaselessAttrDict Example

```python
from caseless_dictionary import SnakeCaselessAttrDict

# Create a SnakeCaselessAttrDict
snake_caseless_attr_dict = SnakeCaselessAttrDict({"  HeLLO WoRLD  ": 1, 2: "two"})
print(snake_caseless_attr_dict)  # Output: {'hello_world': 1, 2: 'two'}

# Accessing the value using attribute notation
print(snake_caseless_attr_dict.hello_world)  # Output: 1
print(snake_caseless_attr_dict.HELLO_WORLD)  # Output: 1

# Accessing the value using Keys
print(snake_caseless_attr_dict["  hello_world  "])  # Output: 1
print(snake_caseless_attr_dict["  HELLO WORLD  "])  # Output: 1

# Accessing non string value
print(snake_caseless_attr_dict[2])  # Output: two

```

### SnakeCaselessAttrDict with Key as Str Only

```python
from caseless_dictionary import SnakeCaselessAttrDict

# Create a SnakeCaselessAttrDict with key_is_str_only set to True
SnakeCaselessAttrDict.key_is_str_only = True
snake_caseless_attr_dict = SnakeCaselessAttrDict({"  HeLLO WoRLD  ": 1})

# Attempt to set a non-string key
try:
    snake_caseless_attr_dict[1] = 2
except TypeError:
    print("TypeError raised as expected when key_is_str_only is True")
```

## Acknowledgments

During the class '(Advanced) Python For Engineers III' taught by [Raymond Hettinger](https://github.com/rhettinger),
Raymond taught us how to inherit from the builtin Python `dict` by creating a Case-insensitive Dict.
I thought this was a wonderful learning experience so I decided to create a project that would build upon what he
taught.