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
from modifiable_items_dictionary.modifiable_items_attribute_dictionary import ModifiableItemsAttrDict
from modifiable_items_dictionary.modifiable_items_dictionary import Key, Value
from caseless_dictionary.cases import (
    snake_case,
    constant_case,
)


class CaselessAttrDict(ModifiableItemsAttrDict):
    """
    Case-insensitive AttrDict where keys that are strings are in snake case.
    If str_only is set to True, keys must be of type str.

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
    >>> caseless_attr_dict.str_only = True
    >>> caseless_attr_dict[1] = 2  # Raises TypeError: Key must be a str, not int
    """

    __slots__ = ()
    _key_modifiers = [snake_case]
    str_only = False


    def __missing__(self, key: Key) -> None:
        """Handle missing __key.
        Args:
            key: The Hashable __key that is missing.

        Raises:
            *KeyError* with a more descriptive error for caseless keys.
        """
        error = KeyError('Missing key of some case variant of ', key)

        raise error

    def __setitem__(self, key: Key, value: Value) -> None:
        """Set the value of the key in the dictionary.
        Args:
            key: The Hashable key that will be set.
            value: The value that will be set for the key.

        Raises:
            TypeError: If str_only is True and key is not a str.
        """
        if self.str_only and not isinstance(key, str):
            raise TypeError("Key must be a str, not ", type(key).__name__)
        ModifiableItemsAttrDict.__setitem__(self, key, value)


class SnakeCaselessAttrDict(CaselessAttrDict):
    """
    Case-insensitive AttrDict where keys that are strings are in snake case.
    If str_only is set to True, keys must be of type str.

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
    >>> snake_caseless_attr_dict.str_only = True
    >>> snake_caseless_attr_dict[1] = 2  # Raises TypeError: Key must be a str, not int
    """
    __slots__ = ()


class ConstantCaselessAttrDict(CaselessAttrDict):
    """
    Case-insensitive AttrDict where keys that are strings are in constant case.
    If str_only is set to True, keys must be of type str.

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
    >>> constant_caseless_attr_dict.str_only = True
    >>> constant_caseless_attr_dict[1] = 2  # Raises TypeError: Key must be a str, not int
    """

    __slots__ = ()
    _key_modifiers = [constant_case]