"""
This module contains examples of how to use the caseless attribute dictionary
classes.

Each function creates a caseless attribute dictionary of a different type and
prints its contents.

Functions:
    example_caseless_attr_dict():
        Creates a SnakeCaselessAttrDict and prints its contents.

    example_constant_caseless_attr_dict():
        Creates a ConstantCaselessAttrDict and prints its contents.
"""
from caseless_dictionary.caseless_attribute_dict import (
    SnakeCaselessAttrDict,
    ConstantCaselessAttrDict,
)


def example_caseless_attr_dict():
    """
    This function creates a SnakeCaselessAttrDict with 'Hello World' and
    'WORLD WIDE' as keys. It then prints the dictionary and the value of the
    'Hello World' key accessed using attribute notation. If a non-string key
    is attempted to be set, a TypeError is raised.
    """
    # Keys can only be strings
    SnakeCaselessAttrDict.key_is_str_only = True
    caseless_attr_dict = SnakeCaselessAttrDict(
        {'   Hello World   ': 1, '   WORLD WIDE   ': 2}
    )
    print(caseless_attr_dict)  # Output: {'hello world': 1, 'world wide': 2}
    print(caseless_attr_dict.hEllo_wOrld)  # Output: 1
    try:
        caseless_attr_dict[1] = 2  # Raises TypeError
    except TypeError:
        print('TypeError raised as expected when str_only is True')


def example_constant_caseless_attr_dict():
    """
    This function creates a ConstantCaselessAttrDict with 'Hello World' and
    'WORLD WIDE' as keys. It then prints the dictionary and the value of the
    'Hello World' key accessed using attribute notation. If a non-string key
    is attempted to be set, a TypeError is raised.
    """
    # Keys can only be strings
    ConstantCaselessAttrDict.key_is_str_only = True
    constant_caseless_attr_dict = ConstantCaselessAttrDict(
        {'   Hello World   ': 1, '   WORLD WIDE   ': 2}
    )
    print(
        constant_caseless_attr_dict
    )  # Output: {'HELLO_WORLD': 1, 'WORLD_WIDE': 2}
    print(constant_caseless_attr_dict.HELLO_WORLD)  # Output: 1
    try:
        constant_caseless_attr_dict[1] = 2  # Raises TypeError
    except TypeError:
        print('TypeError raised as expected when str_only is True')
