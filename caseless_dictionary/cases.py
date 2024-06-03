"""
This module contains a collection of functions that modify the case of a string.

Each function takes an input value and, if the value is a string, it strips
the string and then modifies the case. If the input value is not a string, it
returns the value unchanged.

Functions:
    case_fold(value: Any) -> Any:
        Strips the string and then applies case folding.

    upper(value: Any) -> Any:
        Strips the string and then converts it to uppercase.

    lower(value: Any) -> Any:
        Strips the string and then converts it to lowercase.

    title(value: Any) -> Any:
        Strips the string and then converts it to title case.

    snake_case(value: Any) -> Any:
        Strips the string and then converts it to snake case.

    kebab_case(value: Any) -> Any:
        Strips the string and then converts it to kebab case.

    constant_case(value: Any) -> Any:
        Strips the string and then converts it to constant case.
"""
from typing import Any


def case_fold(value: Any):
    """strip then casefold a *str*

    Example:
        >>> case_fold("   sOme WoRd   ")
        'some word'
        >>> case_fold(2) # Not a *str*
        2

    Args:
        value: If an instance of a string strip then casefold the *v*

    Returns:
        The stripped and casefolded *str*. If not an instance of *str* return
        the v unchanged.

    """
    if isinstance(value, str):
        _stripped_value = value.strip()
        value_case_folded = _stripped_value.casefold()
        return value_case_folded
    return value


def upper(value: Any):
    """strip the string then convert to uppercase.

    Example:
        >>> upper("   sOme WoRd   ")
        'SOME WORD'
        >>> upper(["not of type *str*"]) # Not a *str*
        ['not of type *str*']

    Args:
        value: If an instance of a string strip then convert the *v* to an
            uppercase *str*

    Returns:
        The stripped and uppercased *str*. If not an instance of *str* return
        the v unchanged.
    """
    if isinstance(value, str):
        _stripped_value = value.strip()
        value_upper_case = _stripped_value.upper()
        return value_upper_case
    return value


def lower(value: Any):
    """strip the string then convert to lowercase.

    Example:
        >>> lower("   sOme WoRd   ")
        'some word'
        >>> lower(["not of type *str*"]) # Not a *str*
        ['not of type *str*']

    Args:
        value: If an instance of a string strip then convert the *v* to a
            lowercase *str*

    Returns:
        The stripped and lowercased *str*. If not an instance of *str* return
        the v unchanged.
    """
    if isinstance(value, str):
        _stripped_value = value.strip()
        value_lower_case = _stripped_value.lower()
        return value_lower_case
    return value


def title(value: Any):
    """strip the string then convert to title.

    Example:
        >>> title("   lower UPPER CamelCase   ")
        'Lower Upper Camelcase'
        >>> title(["not of type *str*"]) # Not a *str*
        ['not of type *str*']

    Args:
        value: If an instance of a string strip then convert the *v* to an
            uppercase *str*

    Returns:
        The stripped and uppercased *str*. If not an instance of *str* return
        the v unchanged.
    """
    if isinstance(value, str):
        _stripped_value = value.strip()
        value_title_case = _stripped_value.title()
        return value_title_case
    return value


def snake_case(value: Any):
    """strip the string then convert to snake case.

    Example:
        >>> snake_case("   sOme WoRd   ")
        'some_word'
        >>> snake_case(["not of type *str*"]) # Not a *str*
        ['not of type *str*']

    Args:
        value: If an instance of a string strip then convert the *v* to a
            snake case *str*

    Returns:
        The stripped and snake cased *str*. If not an instance of *str* return
        the v unchanged.
    """
    if isinstance(value, str):
        _stripped_value = value.strip()
        value_snake_case = _stripped_value.replace(' ', '_').casefold()
        return value_snake_case
    return value


def kebab_case(value: Any):
    """strip the string then convert to kebab case.

    Example:
        >>> kebab_case("   sOme WoRd   ")
        'some-word'
        >>> kebab_case(["not of type *str*"]) # Not a *str*
        ['not of type *str*']

    Args:
        value: If an instance of a string strip then convert the *v* to a
            kebab case *str*

    Returns:
        The stripped and kebab cased *str*. If not an instance of *str* return
        the v unchanged.
    """
    if isinstance(value, str):
        _stripped_value = value.strip()
        value_kebab_case = _stripped_value.replace(' ', '-').casefold()
        return value_kebab_case
    return value


def constant_case(value: Any):
    """strip the string then convert to constant case.

    Example:
        >>> constant_case("   sOme WoRd   ")
        'SOME_WORD'
        >>> constant_case(["not of type *str*"]) # Not a *str*
        ['not of type *str*']

    Args:
        value: If an instance of a string strip then convert the *v* to a
            constant case *str*

    Returns:
        The stripped and constant cased *str*. If not an instance of *str*
        return the v unchanged.
    """
    if isinstance(value, str):
        _stripped_value = value.strip()
        value_constant_case = _stripped_value.replace(' ', '_').upper()
        return value_constant_case
    return value
