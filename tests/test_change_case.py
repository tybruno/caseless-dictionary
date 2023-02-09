from typing import Any

import pytest

from caseless_dictionary.caseless_dictionary import _case_fold, _upper, _title


@pytest.fixture(
    params=(
        1,
        5.56,
        True,
        "   Tittle  ",
        "lower  ",
        "   UPPER",
        "CamelCase  ",
        ["NotTouched"],
    )
)
def data(request) -> Any:
    _data: Any = request.param
    return _data


class TestCaseFold:
    def test_case_fold(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().casefold()

        actual = _case_fold(data)
        assert actual == expected


class TestTitle:
    def test_case_fold(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().title()

        actual = _title(data)
        assert actual == expected


class TestUpper:
    def test_case_fold(self, data):
        expected = data
        if isinstance(data, str):
            expected = data.strip().upper()

        actual = _upper(data)
        assert actual == expected
