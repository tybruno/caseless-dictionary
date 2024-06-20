"""
Caseless dictionary is a dictionary that is case-insensitive and allows access
to keys in different cases.

The caseless dictionary module provides the following classes:
    - CaselessDict: A case-insensitive dictionary that allows access to keys in
        different cases.
    - UpperCaselessDict: A case-insensitive dictionary that converts keys to
        uppercase.
    - TitleCaselessDict: A case-insensitive dictionary that converts keys to
        title case.
    - SnakeCaselessDict: A case-insensitive dictionary that converts keys to
        snake case.
    - KebabCaselessDict: A case-insensitive dictionary that converts keys to
        kebab case.
    - ConstantCaselessDict: A case-insensitive dictionary that converts keys to
        constant case.
    - CaselessAttrDict: A case-insensitive dictionary that allows access to
        keys in different cases using attribute access.
    - SnakeCaselessAttrDict: A case-insensitive dictionary that allows access
        to keys in different cases using snake case attribute access.
    - ConstantCaselessAttrDict: A case-insensitive dictionary that allows
        access to keys in different cases using constant case attribute access.
"""
from caseless_dictionary.caseless_attribute_dict import (
    CaselessAttrDict,
    SnakeCaselessAttrDict,
    ConstantCaselessAttrDict,
)
from caseless_dictionary.caseless_dict import (
    CaselessDict,
    UpperCaselessDict,
    TitleCaselessDict,
    SnakeCaselessDict,
    KebabCaselessDict,
    ConstantCaselessDict,
)

__all__ = (
    CaselessDict.__name__,
    UpperCaselessDict.__name__,
    TitleCaselessDict.__name__,
    SnakeCaselessDict.__name__,
    KebabCaselessDict.__name__,
    ConstantCaselessDict.__name__,
    CaselessAttrDict.__name__,
    SnakeCaselessAttrDict.__name__,
    ConstantCaselessAttrDict.__name__,
)
