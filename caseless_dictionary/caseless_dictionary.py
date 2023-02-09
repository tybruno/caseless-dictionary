""" Caseless Dictionary and related objects.

Objects provided by this module:
   `CaselessDict` - Keys are case-folded case.
   `TitleCaselessDict` - Keys are in title case.
   `UpperCaselessDict` - Keys are in upper case.

"""
from typing import (
    Any,
    Hashable,
)

from modifiable_items_dict import ModifiableItemsDict


def _case_fold(value: Any):
    """strip then casefold a *str*

    >>> _case_fold("CamelCase")
    'camelcase'
    >>> _case_fold(2) # Not a *str*
    2

    Args:
        value: If an instance of a string strip then casefold the *v*

    Returns:
        The stripped and casefolded *str*. If not an instance of *str* return the v unchanged.

    """
    if isinstance(value, str):
        _stripped_value: str = value.strip()
        _value_case_folded: str = _stripped_value.casefold()
        return _value_case_folded
    return value


def _upper(value: Any):
    """strip the string then convert to uppercase.
    Example:

    >>> _upper("CamelCase")
    'CAMELCASE'
    >>> _upper(["not of type *str*"]) # Not a *str*
    ['not of type *str*']

    Args:
        value: If an instance of a string strip then convert the *v* to an uppercase *str*

    Returns:
        The stripped and uppercased *str*. If not an instance of *str* return the v unchanged.
    """
    if isinstance(value, str):
        _stripped_value: str = value.strip()
        _value_upper: str = _stripped_value.upper()
        return _value_upper
    return value


def _title(value: Any):
    """strip the string then convert to title.

    >>> _title("lower UPPER CamelCase")
    'Lower Upper Camelcase'
    >>> _title(["not of type *str*"]) # Not a *str*
    ['not of type *str*']

    Args:
        value: If an instance of a string strip then convert the *v* to an uppercase *str*

    Returns:
        The stripped and uppercased *str*. If not an instance of *str* return the v unchanged.
    """
    if isinstance(value, str):
        _stripped_value: str = value.strip()
        _value_title: str = _stripped_value.title()
        return _value_title
    return value


class CaselessDict(ModifiableItemsDict):
    """Case-insensitive Dictionary class where the keys thar are strings are casefolded.

    CaselessDict() -> new empty caseless dictionary
    CaselessDict(mapping) -> new caseless dictionary initialized from a mapping object's
        (__key, v) pairs
    CaselessDict(__m) -> new caseless dictionary initialized as if via:
        d = CaselessDict()
        for k, v in __m:
            d[k] = v
    CaselessDict(**kwargs) -> new caseless dictionary initialized with the name=v pairs
        in the keyword argument list.  For example:  CaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> caseless_dict = CaselessDict(normal_dict)
    >>> caseless_dict
    {'lower': 1, 'upper': 2, 'camelcase': 3}
    >>> caseless_dict[" UPpeR  "]
    2
    """

    _key_modifiers = staticmethod(_case_fold)

    def __missing__(self, key: Hashable) -> None:
        """Handle missing __key.
        Args:
            key: The Hashable __key that is missing.

        Raises:
            *KeyError* with a more descriptive error for caseless keys.
        """
        error: KeyError = KeyError(
            "Missing key of some case variant of ", key
        )

        raise error


class UpperCaselessDict(CaselessDict):
    """Case-insensitive Dictionary class where the keys that are strings are in upper case.

    UpperCaselessDict() -> new empty upper caseless dictionary
    UpperCaselessDict(mapping) -> new upper caseless dictionary initialized from a mapping object's
        (__key, v) pairs
    UpperCaselessDict(__m) -> new upper caseless dictionary initialized as if via:
        d = UpperCaselessDict()
        for k, v in __m:
            d[k] = v
    UpperCaselessDict(**kwargs) -> new upper caseless dictionary initialized with the name=v pairs
        in the keyword argument list.  For example:  UpperCaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> upper_caseless_dict = UpperCaselessDict(normal_dict)
    >>> upper_caseless_dict
    {'LOWER': 1, 'UPPER': 2, 'CAMELCASE': 3}
    >>> "CAmelCase  " in upper_caseless_dict
    True
    """

    _key_modifiers = staticmethod(_upper)


class TitleCaselessDict(CaselessDict):
    """Case-insensitive Dictionary class where the keys that are strings are in Title Case.

    TitleCaselessDict() -> new empty title caseless dictionary
    TitleCaselessDict(mapping) -> new title caseless dictionary initialized from a mapping object's
        (__key, v) pairs
    TitleCaselessDict(__m) -> new title caseless dictionary initialized as if via:
        d = TitleCaselessDict()
        for k, v in __m:
            d[k] = v
    TitleCaselessDict(**kwargs) -> new title caseless dictionary initialized with the name=v pairs
        in the keyword argument list.  For example:  TitleCaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> upper_caseless_dict = TitleCaselessDict(lower=1, UPPER=2, CamelCase=3)
    >>> upper_caseless_dict
    {'Lower': 1, 'Upper': 2, 'Camelcase': 3}
    >>> "  lOwEr  " in upper_caseless_dict
    True
    """

    _key_modifiers = staticmethod(_title)
