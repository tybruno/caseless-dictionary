"""
This module contains classes that implement case-insensitive attribute
dictionaries.

Classes:
    - CaselessAttrDict: A case-insensitive AttrDict where keys that are
        strings are in snake case.
    - SnakeCaselessAttrDict: A case-insensitive AttrDict where keys that are
        strings are in snake case.
    - ConstantCaselessAttrDict: A case-insensitive AttrDict where keys that
        are strings are in constant case.

Each class inherits from ModifiableItemsAttrDict and overrides the
_key_modifiers attribute to provide different case handling.
"""
from modifiable_items_dictionary import ModifiableItemsAttrDict
from caseless_dictionary.cases import (
    snake_case,
    constant_case,
)


class CaselessAttrDict(ModifiableItemsAttrDict):
    """
    Case-insensitive AttrDict where keys that are strings are in snake case.

    CaselessAttrDict() -> new empty caseless attribute dictionary
    CaselessAttrDict(mapping) -> new caseless attribute dictionary initialized
        from a mapping object's (key, value) pairs
    CaselessAttrDict(iterable) -> new caseless attribute dictionary initialized
        as if via:
        d = CaselessAttrDict()
        for k, v in iterable:
            d[k] = v
    CaselessAttrDict(**kwargs) -> new caseless attribute dictionary initialized
        with the name=value pairs in the keyword argument list.
        For example:  CaselessAttrDict(one=1, two=2)


    Example:
    >>> normal_dict: dict = {" sOmE WoRD ":1}
    >>> caseless_attr_dict = CaselessAttrDict(normal_dict)
    >>> caseless_attr_dict
    {'some_word': 1}
    >>> caseless_attr_dict["soME_WorD"]
    1
    >>> caseless_attr_dict.sOme_worD
    1

    """

    __slots__ = ()
    _key_modifiers = [snake_case]


class SnakeCaselessAttrDict(CaselessAttrDict):
    """
    Case-insensitive AttrDict where keys that are strings are in snake case.

    SnakeCaselessAttrDict() -> new empty snake caseless attribute dictionary
    SnakeCaselessAttrDict(mapping) -> new snake caseless attribute dictionary
        initialized from a mapping object's (key, value) pairs
    SnakeCaselessAttrDict(iterable) -> new snake caseless attribute dictionary
        initialized as if via:
        d = SnakeCaselessAttrDict()
        for k, v in iterable:
            d[k] = v
    SnakeCaselessAttrDict(**kwargs) -> new snake caseless attribute dictionary
        initialized with the name=value pairs in the keyword argument list.
        For example:  SnakeCaselessAttrDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {" sOmE WoRD ":1}
    >>> snake_caseless_attr_dict = SnakeCaselessAttrDict(normal_dict)
    >>> snake_caseless_attr_dict
    {'some_word': 1}
    >>> snake_caseless_attr_dict["soME_WorD"]
    1
    >>> snake_caseless_attr_dict.sOme_worD
    1
    """

    __slots__ = ()


class ConstantCaselessAttrDict(CaselessAttrDict):
    """
    Case-insensitive AttrDict where keys that are strings are in constant case.

    ConstantCaselessAttrDict() -> new empty constant caseless attribute dict
    ConstantCaselessAttrDict(mapping) -> new constant caseless attribute dict
        initialized from a mapping object's (key, value) pairs
    ConstantCaselessAttrDict(iterable) -> new constant caseless attribute dict
        initialized as if via:
        d = ConstantCaselessAttrDict()
        for k, v in iterable:
            d[k] = v
    ConstantCaselessAttrDict(**kwargs) -> new constant caseless attribute dict
        initialized with the name=value pairs in the keyword argument list.
        For example:  ConstantCaselessAttrDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {" sOmE WoRD ":1}
    >>> constant_caseless_attr_dict = ConstantCaselessAttrDict(normal_dict)
    >>> constant_caseless_attr_dict
    {'SOME_WORD': 1}
    >>> constant_caseless_attr_dict["soME_WorD"]
    1
    >>> constant_caseless_attr_dict.sOme_worD
    1
    """

    __slots__ = ()
    _key_modifiers = [constant_case]
