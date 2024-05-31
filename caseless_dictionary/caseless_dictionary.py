"""
Caseless Dictionary and related objects.

Objects provided by this module:
   `CaselessDict` - Keys are case-folded case.
   `TitleCaselessDict` - Keys are in title case.
   `UpperCaselessDict` - Keys are in upper case.
   `SnakeCaselessDict` - Keys are in snake case.
   `KebabCaselessDict` - Keys are in kebab case.
   `ConstantCaselessDict` - Keys are in constant case.
"""
from modifiable_items_dictionary.modifiable_items_dictionary import ModifiableItemsDict,Key, Value

from caseless_dictionary.cases import (
    case_fold,
    upper,
    lower,
    title,
    snake_case,
    kebab_case,
    constant_case,
)


class CaselessDict(ModifiableItemsDict):
    """
    Case-insensitive Dictionary class where the keys that are strings are
    casefolded. If str_only is set to True, keys must be of type str.

    CaselessDict() -> new empty caseless dictionary
    CaselessDict(mapping) -> new caseless dictionary initialized from a
        mapping object's (key, value) pairs
    CaselessDict(iterable) -> new caseless dictionary initialized as if via:
        d = CaselessDict()
        for k, v in iterable:
            d[k] = v
    CaselessDict(**kwargs) -> new caseless dictionary initialized with
        the name=value pairs in the keyword argument list.
        For example:  CaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> caseless_dict = CaselessDict(normal_dict)
    >>> caseless_dict
    {'lower': 1, 'upper': 2, 'camelcase': 3}
    >>> caseless_dict[" UPpeR  "]
    2
    >>> caseless_dict.str_only = True
    >>> caseless_dict[1] = 2  # Raises TypeError: Key must be a str, not int
    """

    __slots__ = ()
    _key_modifiers = [case_fold]
    str_only = False

    def __missing__(self, key: Key) -> None:
        """Handle missing key.
        Args:
            key: The Hashable key that is missing.

        Raises:
            KeyError: with a more descriptive error for caseless keys.
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

        ModifiableItemsDict.__setitem__(self, key, value)


class CaseFoldCaselessDict(CaselessDict):
    """
    Case-insensitive Dictionary class where keys that are strings are
    case-folded. If str_only is True, keys must be str.

    CaseFoldCaselessDict() -> new empty case-folded caseless dictionary
    CaseFoldCaselessDict(mapping) -> new case-folded caseless dictionary
        initialized from a mapping object's (key, value) pairs
    CaseFoldCaselessDict(iterable) -> new case-folded caseless dictionary
        initialized as if via:
        d = CaseFoldCaselessDict()
        for k, v in iterable:
            d[k] = v
    CaseFoldCaselessDict(**kwargs) -> new case-folded caseless dictionary
        initialized with the name=value pairs in the keyword argument list.
        For example:  CaseFoldCaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> case_fold_caseless_dict = CaseFoldCaselessDict(normal_dict)
    >>> case_fold_caseless_dict
    {'lower': 1, 'upper': 2, 'camelcase': 3}
    >>> case_fold_caseless_dict[" UPpeR  "]
    2
    >>> case_fold_caseless_dict.str_only = True
    >>> case_fold_caseless_dict[1] = 2  # Raises TypeError
    """

    __slots__ = ()


class LowerCaselessDict(CaselessDict):
    """
    Case-insensitive Dictionary class where keys that are strings are
    in lower case. If str_only is True, keys must be str.

    LowerCaselessDict() -> new empty lower caseless dictionary
    LowerCaselessDict(mapping) -> new lower caseless dictionary
        initialized from a mapping object's (key, value) pairs
    LowerCaselessDict(iterable) -> new lower caseless dictionary
        initialized as if via:
        d = LowerCaselessDict()
        for k, v in iterable:
            d[k] = v
    LowerCaselessDict(**kwargs) -> new lower caseless dictionary
        initialized with the name=value pairs in the keyword argument list.
        For example:  LowerCaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> lower_caseless_dict = LowerCaselessDict(normal_dict)
    >>> lower_caseless_dict
    {'lower': 1, 'upper': 2, 'camelcase': 3}
    >>> lower_caseless_dict[" UPpeR  "]
    2
    >>> lower_caseless_dict.str_only = True
    >>> lower_caseless_dict[1] = 2  # Raises TypeError
    """

    __slots__ = ()
    _key_modifiers = [lower]


class UpperCaselessDict(CaselessDict):
    """
    Case-insensitive Dictionary class where keys that are strings are
    in upper case. If str_only is True, keys must be str.

    UpperCaselessDict() -> new empty upper caseless dictionary
    UpperCaselessDict(mapping) -> new upper caseless dictionary initialized
        from a mapping object's (key, value) pairs
    UpperCaselessDict(iterable) -> new upper caseless dictionary initialized
        as if via:
        d = UpperCaselessDict()
        for k, v in iterable:
            d[k] = v
    UpperCaselessDict(**kwargs) -> new upper caseless dictionary initialized
        with the name=value pairs in the keyword argument list.
        For example:  UpperCaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> upper_caseless_dict = UpperCaselessDict(normal_dict)
    >>> upper_caseless_dict
    {'LOWER': 1, 'UPPER': 2, 'CAMELCASE': 3}
    >>> "CAmelCase  " in upper_caseless_dict
    True
    >>> upper_caseless_dict.str_only = True
    >>> upper_caseless_dict[1] = 2  # Raises TypeError
    """

    __slots__ = ()
    _key_modifiers = [upper]


class TitleCaselessDict(CaselessDict):
    """
    Case-insensitive Dictionary class where keys that are strings are
    in Title Case. If str_only is True, keys must be str.

    TitleCaselessDict() -> new empty title caseless dictionary
    TitleCaselessDict(mapping) -> new title caseless dictionary initialized
        from a mapping object's (key, value) pairs.
    TitleCaselessDict(iterable) -> new title caseless dictionary initialized
        as if via:
        d = TitleCaselessDict()
        for k, v in iterable:
            d[k] = v
    TitleCaselessDict(**kwargs) -> new title caseless dictionary initialized
        with the name=value pairs in the keyword argument list.
        For example:  TitleCaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> upper_caseless_dict = TitleCaselessDict(lower=1, UPPER=2, CamelCase=3)
    >>> upper_caseless_dict
    {'Lower': 1, 'Upper': 2, 'Camelcase': 3}
    >>> "  lOwEr  " in upper_caseless_dict
    True
    >>> upper_caseless_dict.str_only = True
    >>> upper_caseless_dict[1] = 2  # Raises TypeError
    """

    __slots__ = ()
    _key_modifiers = [title]


class SnakeCaselessDict(CaselessDict):
    """
    Case-insensitive Dictionary class where keys that are strings are
    in Snake Case. If str_only is True, keys must be str.

    SnakeCaselessDict() -> new empty snake caseless dictionary
    SnakeCaselessDict(mapping) -> new snake caseless dictionary initialized
        from a mapping object's (key, value) pairs
    SnakeCaselessDict(iterable) -> new snake caseless dictionary initialized
        as if via:
        d = SnakeCaselessDict()
        for k, v in iterable:
            d[k] = v
    SnakeCaselessDict(**kwargs) -> new snake caseless dictionary initialized
        with the name=value pairs in the keyword argument list.
        For example:  SnakeCaselessDict(one=1, two=2)

    Example:
    >>> from caseless_dictionary import SnakeCaselessDict
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> snake_caseless_dict = SnakeCaselessDict(lower=1, UPPER=2, CamelCase=3)
    >>> snake_caseless_dict
    {'lower': 1, 'upper': 2, 'camel_case': 3}
    >>> "  CamelCase  " in snake_caseless_dict
    True
    >>> snake_caseless_dict.str_only = True
    >>> snake_caseless_dict[1] = 2  # Raises TypeError
    """

    __slots__ = ()
    _key_modifiers = [snake_case]


class KebabCaselessDict(CaselessDict):
    """
    Case-insensitive Dictionary class where keys that are strings are
    in Kebab Case. If str_only is True, keys must be str.

    KebabCaselessDict() -> new empty kebab caseless dictionary
    KebabCaselessDict(mapping) -> new kebab caseless dictionary initialized
        from a mapping object's (key, value) pairs
    KebabCaselessDict(iterable) -> new kebab caseless dictionary initialized
        as if via:
        d = KebabCaselessDict()
        for k, v in iterable:
            d[k] = v
    KebabCaselessDict(**kwargs) -> new kebab caseless dictionary initialized
        with the name=value pairs in the keyword argument list.
        For example:  KebabCaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> kebab_caseless_dict = KebabCaselessDict(lower=1, UPPER=2, CamelCase=3)
    >>> kebab_caseless_dict
    {'lower': 1, 'upper': 2, 'camel-case': 3}
    >>> "  CamelCase  " in kebab_caseless_dict
    True
    >>> kebab_caseless_dict.str_only = True
    >>> kebab_caseless_dict[1] = 2  # Raises TypeError
    """

    __slots__ = ()
    _key_modifiers = [kebab_case]


class ConstantCaselessDict(CaselessDict):
    """
    Case-insensitive Dictionary class where keys that are strings are
    in Constant Case. If str_only is True, keys must be str.

    ConstantCaselessDict() -> new empty constant caseless dictionary
    ConstantCaselessDict(mapping) -> new constant caseless dictionary
        initialized from a mapping object's (key, value) pairs
    ConstantCaselessDict(iterable) -> new constant caseless dictionary
        initialized as if via:
        d = ConstantCaselessDict()
        for k, v in iterable:
            d[k] = v
    ConstantCaselessDict(**kwargs) -> new constant caseless dictionary
        initialized with the name=value pairs in the keyword argument list.
        For example:  ConstantCaselessDict(one=1, two=2)

    Example:
    >>> normal_dict: dict = {"  lower   ": 1, "UPPER ": 2, "CamelCase": 3}
    >>> constant_caseless_dict = ConstantCaselessDict(lower=1, UPPER=2,
    ... CamelCase=3)
    >>> constant_caseless_dict
    {'LOWER': 1, 'UPPER': 2, 'CAMEL_CASE': 3}
    >>> "  CamelCase  " in constant_caseless_dict
    True
    >>> constant_caseless_dict.str_only = True
    >>> constant_caseless_dict[1] = 2  # Raises TypeError
    """

    __slots__ = ()
    _key_modifiers = [constant_case]