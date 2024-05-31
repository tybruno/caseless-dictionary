"""
This module contains examples of how to use the caseless dictionary classes.

Each function creates a caseless dictionary of a different type and prints
its contents.

Functions:
    example_caseless_dict():
        Creates a CaselessDict and prints its contents.

    example_upper_caseless_dict():
        Creates an UpperCaselessDict and prints its contents.

    example_title_caseless_dict():
        Creates a TitleCaselessDict and prints its contents.

    example_snake_caseless_dict():
        Creates a SnakeCaselessDict and prints its contents.

    example_kebab_caseless_dict():
        Creates a KebabCaselessDict and prints its contents.

    example_constant_caseless_dict():
        Creates a ConstantCaselessDict and prints its contents.
"""
from caseless_dictionary.caseless_dictionary import (
    CaselessDict,
    UpperCaselessDict,
    TitleCaselessDict,
    SnakeCaselessDict,
    KebabCaselessDict,
    ConstantCaselessDict,
)


def example_caseless_dict():
    """
    Create a CaselessDict and print its contents. The dictionary is created
    with 'Hello World' and 'WORLD WIDE' as keys.
    """
    caseless_dict = CaselessDict({'Hello World': 1, 'WORLD WIDE': 2})
    print(caseless_dict)  # Output: {'hello world': 1, 'world wide': 2}
    caseless_dict.str_only = True
    try:
        caseless_dict[1] = 2  # Raises TypeError
    except TypeError:
        print("TypeError raised as expected when str_only is True")


def example_upper_caseless_dict():
    """
    Create an UpperCaselessDict and print its contents. The dictionary is
    created with 'Hello World' and 'WORLD WIDE' as keys.
    """
    upper_caseless_dict = UpperCaselessDict(
        {'Hello World': 1, 'WORLD WIDE': 2}
    )
    print(upper_caseless_dict)  # Output: {'HELLO WORLD': 1, 'WORLD WIDE': 2}
    upper_caseless_dict.str_only = True
    try:
        upper_caseless_dict[1] = 2  # Raises TypeError
    except TypeError:
        print("TypeError raised as expected when str_only is True")


def example_title_caseless_dict():
    """
    Create a TitleCaselessDict and print its contents. The dictionary is
    created with 'Hello World' and 'WORLD WIDE' as keys.
    """
    title_caseless_dict = TitleCaselessDict(
        {'Hello World': 1, 'WORLD WIDE': 2}
    )
    print(title_caseless_dict)  # Output: {'Hello World': 1, 'World Wide': 2}
    title_caseless_dict.str_only = True
    try:
        title_caseless_dict[1] = 2  # Raises TypeError
    except TypeError:
        print("TypeError raised as expected when str_only is True")


def example_snake_caseless_dict():
    """
    Create a SnakeCaselessDict and print its contents. The dictionary is
    created with 'Hello World' and 'WORLD WIDE' as keys.
    """
    snake_caseless_dict = SnakeCaselessDict(
        {'Hello World': 1, 'WORLD WIDE': 2}
    )
    print(snake_caseless_dict)  # Output: {'hello_world': 1, 'world_wide': 2}
    snake_caseless_dict.str_only = True
    try:
        snake_caseless_dict[1] = 2  # Raises TypeError
    except TypeError:
        print("TypeError raised as expected when str_only is True")


def example_kebab_caseless_dict():
    """
    Create a KebabCaselessDict and print its contents. The dictionary is
    created with 'Hello World' and 'WORLD WIDE' as keys.
    """
    kebab_caseless_attr_dict = KebabCaselessDict(
        {'Hello World': 1, 'WORLD WIDE': 2}
    )
    print(
        kebab_caseless_attr_dict
    )  # Output: {'hello-world': 1, 'world-wide': 2}
    kebab_caseless_attr_dict.str_only = True
    try:
        kebab_caseless_attr_dict[1] = 2  # Raises TypeError
    except TypeError:
        print("TypeError raised as expected when str_only is True")


def example_constant_caseless_dict():
    """
    Create a ConstantCaselessDict and print its contents. The dictionary is
    created with 'Hello World' and 'WORLD WIDE' as keys.
    """
    constant_caseless_attr_dict = ConstantCaselessDict(
        {'Hello World': 1, 'WORLD WIDE': 2}
    )
    print(
        constant_caseless_attr_dict
    )  # Output: {'HELLO_WORLD': 1, 'WORLD_WIDE': 2}
    constant_caseless_attr_dict.str_only = True
    try:
        constant_caseless_attr_dict[1] = 2  # Raises TypeError
    except TypeError:
        print("TypeError raised as expected when str_only is True")