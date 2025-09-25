
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PyPI version](https://img.shields.io/pypi/v/caseless-dictionary.svg)](https://pypi.org/project/caseless-dictionary/)
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/tybruno/caseless-dictionary)
[![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/codeexchange/devenv/tybruno/caseless-dictionary/)
[![codecov](https://codecov.io/gh/tybruno/caseless-dictionary/branch/main/graph/badge.svg?token=ZO94EJFI3G)](https://codecov.io/gh/tybruno/caseless-dictionary)
[![Pylint](https://img.shields.io/badge/Pylint-10.0%2F10-green)](10.0/10)
[![Mypy](https://img.shields.io/badge/Mypy-checked-blue)](10.0/10)
[![Code Style: Blue](https://img.shields.io/badge/code%20style-blue-0000ff.svg)](https://github.com/psf/blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)

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
## Use Cases

### Network Engineering

Network engineers often work with device configurations, network responses, or protocol data where key names may vary in case or format. Caseless dictionaries simplify parsing and managing such data:
### Using SnakeCaselessDict and ConstantCaselessDict

```python
# Example: Parsing device configuration with snake/constant case
snake_config = SnakeCaselessDict({"Interface Name": "GigabitEthernet0/1"})
print(snake_config["interface_name"])  # Output: 'GigabitEthernet0/1'

constant_config = ConstantCaselessDict({"Interface Name": "GigabitEthernet0/1"})
print(constant_config["INTERFACE_NAME"])  # Output: 'GigabitEthernet0/1'
```

```python
# Example: Parsing device configuration
config = CaselessDict({"Hostname": "router1", "INTERFACE": "GigabitEthernet0/1"})
print(config["hostname"])  # Output: 'router1'
print(config["interface"])  # Output: 'GigabitEthernet0/1'
```

### DevOps

DevOps engineers frequently handle environment variables, configuration files, and automation scripts where key case can be inconsistent. Caseless dictionaries ensure reliable access regardless of case:
### Using Attribute Dicts for Configs

```python
# Example: Accessing config values with attribute notation
from caseless_dictionary import SnakeCaselessAttrDict
config = SnakeCaselessAttrDict({"Log Path": "/var/log/app.log"})
print(config.log_path)  # Output: '/var/log/app.log'
```

```python
# Example: Managing environment variables
import os
env_vars = CaselessDict(os.environ)
print(env_vars["PATH"])  # Works even if the key is 'Path', 'path', etc.
```

### API Integration & Data Normalization

When integrating with external APIs or working with data from multiple sources, key names may differ in case or style. Caseless dictionaries help normalize and access data easily:
### Using KebabCaselessDict for API Data

```python
# Example: Normalizing API keys to kebab-case
from caseless_dictionary import KebabCaselessDict
api_data = KebabCaselessDict({"User Name": "alice", "EMAIL Address": "alice@example.com"})
print(api_data["user-name"])  # Output: 'alice'
print(api_data["email-address"])  # Output: 'alice@example.com'
```

```python
# Example: Handling API response
response = CaselessDict({"UserName": "alice", "EMAIL": "alice@example.com"})
print(response["username"])  # Output: 'alice'
print(response["email"])     # Output: 'alice@example.com'
```

### KafkaSafeDictionary Example

You can create a custom Kafka-safe dictionary by subclassing a caseless dictionary and using key and value modifiers. This ensures keys are case-insensitive, string-only, and values are non-empty strings (safe for Kafka topics, configs, or messages):

```python
from caseless_dictionary import SnakeCaselessDict

def kafka_safe_value(value):
  value = value.strip()
  # Only allow non-empty strings
  if not isinstance(value, str):
    raise ValueError("Kafka values must be strings")
  if not value:
    raise ValueError("Kafka values cannot be empty strings")
  return value

class KafkaSafeDictionary(SnakeCaselessDict):
  _value_modifiers = [kafka_safe_value]
  key_is_str_only = True

# Usage example
kafka_dict = KafkaSafeDictionary({"Kafka Field": "Some Value", "Another Field": "Another Value"})
print(kafka_dict["kafka_field"])  # Output: 'Some Value'
print(kafka_dict["another_field"])  # Output: 'Another Value'

# Attempt to set a non-string key
try:
  kafka_dict[123] = "Invalid Key"
except TypeError:
  print("TypeError: Key must be a string")

# Attempt to set an empty string value
try:
  kafka_dict["empty_field"] = "   "
except ValueError:
  print("ValueError: Kafka values cannot be empty strings")

# Attempt to set a non-string value
try:
  kafka_dict["bad_field"] = 123
except ValueError:
  print("ValueError: Kafka values must be strings")
```

### More Use Cases

- **Configuration Management**: Load and merge config files with varying key cases.
- **Data Cleaning**: Normalize keys in datasets for analysis.
- **Scripting & Automation**: Write robust scripts that work with unpredictable key formats.

## Acknowledgments

During the class '(Advanced) Python For Engineers III' taught by [Raymond Hettinger](https://github.com/rhettinger),
Raymond taught us how to inherit from the builtin Python `dict` by creating a Case-insensitive Dict.
I thought this was a wonderful learning experience so I decided to create a project that would build upon what he
taught.