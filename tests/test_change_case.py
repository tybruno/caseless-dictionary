"""Test cases for the change_case module.

This module contains test cases for the change_case module. It tests the
functions that change the case of a string.

Classes:
    TestCaseFold: Test case for the case_fold function.
    TestTitle: Test case for the title function.
    TestUpper: Test case for the upper function.
    TestLowerCase: Test case for the lower function.
    TestSnakeCase: Test case for the snake_case function.
    TestKebabCase: Test case for the kebab_case function.
"""
import typing
import re
import pytest

from caseless_dictionary.cases import (
    case_fold,
    upper,
    title,
    snake_case,
    kebab_case,
    lower,
    constant_case,
)


@pytest.fixture(
    params=(
        1,
        5.56,
        True,
        '   Tittle  ',
        'lower  ',
        '   UPPER',
        'CamelCase  ',
        ['NotTouched'],
    )
)
def data(request) -> typing.Any:
    _data: typing.Any = request.param
    return _data


class TestCaseFold:
    def test_case_fold(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().casefold()

        actual = case_fold(data)
        assert actual == expected


class TestTitle:
    def test_case_fold(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().title()

        actual = title(data)
        assert actual == expected


class TestUpper:
    def test_case_fold(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().upper()

        actual = upper(data)
        assert actual == expected


class TestSnakeCase:
    def test_snake_case(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().replace(' ', '_').casefold()

        actual = snake_case(data)
        assert actual == expected


class TestKebabCase:
    def test_kebab_case(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().replace(' ', '-').casefold()

        actual = kebab_case(data)
        assert actual == expected


class TestConstantCase:
    def test_constant_case(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().replace(' ', '_').upper()

        actual = constant_case(data)
        assert actual == expected


class TestLowerCase:
    def test_lower_case(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().lower()

        actual = lower(data)
        assert actual == expected
