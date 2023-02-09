import contextlib
from copy import deepcopy
from typing import Mapping, Any, Callable, Hashable, NamedTuple, Type

import pytest

from caseless_dictionary.caseless_dictionary import (
    CaselessDict,
    TitleCaselessDict,
    UpperCaselessDict,
)


class _TestingClass(NamedTuple):
    cls: Type[CaselessDict]
    key_modifier: Callable[[Any], Hashable]


def _case_fold(value: Any):
    if isinstance(value, str):
        value = value.strip().casefold()
    return value


def _upper(value: Any):
    if isinstance(value, str):
        value = value.strip().upper()
    return value


def _title(value: Any):
    if isinstance(value, str):
        value = value.strip().title()
    return value


@pytest.fixture(
    params=(
        {
            "CamelCase": 1,
            "lower": 2,
            "UPPER": 3,
            "snake_case": 4,
            5.56: "Five",
            True: "True",
        },
        {1: 2, ("hello", "Goodbye"): 2},
    )
)
def valid_mapping(request) -> Mapping:
    inputs: Mapping = request.param
    return inputs


@pytest.fixture(
    params=(
        _TestingClass(CaselessDict, _case_fold),
        _TestingClass(UpperCaselessDict, _upper),
        _TestingClass(TitleCaselessDict, _title),
    )
)
def caseless_class(request) -> _TestingClass:
    _caseless_class: _TestingClass = request.param
    return _caseless_class


@pytest.fixture(params=(set(), list(), dict()))
def unhashable_type(request):
    unhashable_type = request.param
    return unhashable_type


class TestCaselessDictionary:
    def test__init__mapping(
        self, valid_mapping: Mapping, caseless_class: _TestingClass
    ):
        _class, _key_operation = caseless_class
        caseless_dictionary = _class(valid_mapping)
        expected = {
            _key_operation(key): value for key, value in valid_mapping.items()
        }
        assert caseless_dictionary == expected

    @pytest.mark.parametrize(
        "valid_kwargs",
        ({"a": 1, "B": 2}, {"lower": 3, "UPPER": 4, "MiXeD": 5}),
    )
    def test__init__kwargs(self, valid_kwargs, caseless_class):
        _class, _key_operation = caseless_class

        caseless_dictionary = _class(**valid_kwargs)
        expected = {
            _key_operation(key): value for key, value in valid_kwargs.items()
        }
        assert caseless_dictionary == expected

    @pytest.mark.parametrize(
        "mapping_and_kwargs",
        [
            ({"a": 1, "B": 2}, {"lower": 3, "UPPER": 4, "MiXeD": 5}),
        ],
    )
    def test__init__iterable_and_kwargs(
        self, mapping_and_kwargs, caseless_class
    ):
        _class, _key_operation = caseless_class
        args, kwargs = mapping_and_kwargs
        expected = {
            _key_operation(key): value
            for key, value in dict(**args, **kwargs).items()
        }
        caseless_dictionary = _class(args, **kwargs)
        assert caseless_dictionary == expected

    @pytest.mark.parametrize(
        "iterables",
        [
            zip(["one", "TwO", "ThrEE"], [1, 2, 3]),
            [("TwO", 2), ("one", 1), ("ThrEE", 3), (4, "FouR")],
        ],
    )
    def test__init__iterable(self, iterables, caseless_class):
        _class, _key_operation = caseless_class
        iterables_copy = deepcopy(iterables)
        caseless_dictionary = _class(iterables)
        expected: Mapping = {
            _key_operation(key): value for key, value in iterables_copy
        }
        assert caseless_dictionary == expected
        assert repr(caseless_dictionary) == repr(expected)

    @pytest.mark.parametrize("invalid_type", ([1], {2}, True, 1))
    def test__init__invalid_type(self, invalid_type, caseless_class):
        _class, _ = caseless_class

        with pytest.raises(TypeError):
            _class(invalid_type)

    @pytest.mark.parametrize("iterable", [[("1", 1), ("two", 2, 2)]])
    def test__init__bad_iterable_elements(self, iterable, caseless_class):
        _class, _ = caseless_class

        with pytest.raises(ValueError):
            _class(iterable)

    @pytest.mark.parametrize(
        "keys",
        (["lower", "Title", "UPPER", "CamelCase", "snake_case", object()],),
    )
    def test_fromkeys(self, keys, caseless_class):
        _class, _key_operation = caseless_class

        value = None
        expected: Mapping = {_key_operation(key): value for key in keys}

        caseless_dictionary = _class.fromkeys(keys, value)
        assert caseless_dictionary == expected
        assert isinstance(caseless_dictionary, _class)

        for key in keys:
            assert key in caseless_dictionary

    @pytest.mark.parametrize("invalid_type", (True, 1))
    def test_fromkeys_with_invalid_type(self, invalid_type, caseless_class):
        _class, _ = caseless_class

        with pytest.raises(TypeError):
            _class.fromkeys(invalid_type)

    def test__setitem__(self, valid_mapping, caseless_class):
        _class, _key_operation = caseless_class

        caseless_dict: _class = _class()
        expected: dict = dict()
        for key, item in valid_mapping.items():
            expected[_key_operation(key)] = item
            caseless_dict[key] = item
        assert caseless_dict == expected
        assert repr(caseless_dict) == repr(expected)

    def test___setitem__bad_key_type(self, caseless_class, unhashable_type):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class()
        with pytest.raises(TypeError):
            caseless_dictionary[unhashable_type] = 0

    def test__getitem__(self, valid_mapping, caseless_class):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class(valid_mapping)
        for key, value in valid_mapping.items():
            assert caseless_dictionary[key] == value

    def test__getitem__missing_key(self, caseless_class):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class()
        assert caseless_dictionary == dict()

        # make unique __key which will not be in dict
        _missing_key = object()

        with pytest.raises(KeyError):
            _ = caseless_dictionary[_missing_key]

    def test__delitem__(self, valid_mapping, caseless_class):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class(valid_mapping)
        for key, value in valid_mapping.items():
            del caseless_dictionary[key]
            assert key not in caseless_dictionary

    def test__delitem__missing_key(self, valid_mapping, caseless_class):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class(valid_mapping)
        with contextlib.suppress(KeyError):
            del caseless_dictionary["missing_key"]

    def test_get(self, valid_mapping, caseless_class):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class(valid_mapping)
        for key, value in valid_mapping.items():
            assert caseless_dictionary.get(key) == value
            assert caseless_dictionary.get(key, None) == value

    def test_get_missing_key(self, caseless_class):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class()

        # make unique __key which will not be in dict
        _missing_key = object()
        _default = "__default v"

        assert caseless_dictionary.get(_missing_key) is None
        assert caseless_dictionary.get(_missing_key, _default) == _default

    def test_get_unhashable_key(self, caseless_class, unhashable_type):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class()

        _default = "__default v"

        with pytest.raises(TypeError):
            caseless_dictionary.get(unhashable_type)
            caseless_dictionary.get(unhashable_type, _default)

    def test_pop(self, valid_mapping, caseless_class):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class(valid_mapping)
        for key, value in valid_mapping.items():
            assert caseless_dictionary.pop(key) == value
            assert key not in caseless_dictionary

    def test_pop_missing_key(self, caseless_class):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class()

        # make unique __key which will not be in dict
        _missing_key = object()

        with pytest.raises(KeyError):
            caseless_dictionary.pop(_missing_key)

    def test_pop_unhashable_type(self, caseless_class, unhashable_type):
        _class, _ = caseless_class

        caseless_dictionary: _class = _class()

        with pytest.raises(KeyError):
            caseless_dictionary.pop(unhashable_type)

    def test_setdefault(self, valid_mapping, caseless_class):
        _class, _key_operation = caseless_class

        caseless_dict: _class = _class()
        expected: dict = dict()
        for key, item in valid_mapping.items():
            expected.setdefault(_key_operation(key), item)
            caseless_dict.setdefault(key, item)
        assert caseless_dict == expected
        assert repr(caseless_dict) == repr(expected)

    def test_setdefault_unhashable_type(
        self, caseless_class, unhashable_type
    ):
        _class, _key_operation = caseless_class

        caseless_dict: _class = _class()

        with pytest.raises(TypeError):
            caseless_dict.setdefault(unhashable_type)

    @pytest.mark.parametrize(
        "starting_data", ({"start_lower": 1, "START_UPPER": 2, "__key": 1},)
    )
    @pytest.mark.parametrize(
        "args", ({"UPPER": 1, "lower": 2, "CamelCase": 3, "Key": 2},)
    )
    @pytest.mark.parametrize("kwargs", ({"UP": 1, "down": 2, "__key": 3},))
    def test_update_using_mapping(
        self, caseless_class, starting_data, args, kwargs
    ):
        _class, _key_operation = caseless_class
        caseless_dict: _class = _class(starting_data)

        expected = dict(
            {
                _key_operation(key): value
                for key, value in starting_data.items()
            }
        )

        assert caseless_dict == expected

        expected.update(
            {_key_operation(key): value for key, value in args.items()},
            **{_key_operation(key): value for key, value in kwargs.items()}
        )

        caseless_dict.update(args, **kwargs)

        assert caseless_dict == expected

    @pytest.mark.parametrize(
        "starting_data", ({"start_lower": 1, "START_UPPER": 2, "__key": 1},)
    )
    @pytest.mark.parametrize(
        "args",
        ([("UPPER", 1), ("lower", 2), ("CamelCase", 3), ("__key", 2)],),
    )
    @pytest.mark.parametrize("kwargs", ({"UP": 1, "down": 2, "__key": 3},))
    def test_update_using_sequence(
        self, caseless_class, starting_data, args, kwargs
    ):
        _class, _key_operation = caseless_class
        caseless_dict: _class = _class(starting_data)

        expected = dict(
            {
                _key_operation(key): value
                for key, value in starting_data.items()
            }
        )

        assert caseless_dict == expected

        expected.update(
            {_key_operation(key): value for key, value in args},
            **{_key_operation(key): value for key, value in kwargs.items()}
        )

        caseless_dict.update(args, **kwargs)

        assert caseless_dict == expected

    def test_update_unhashable_key(self, caseless_class, unhashable_type):
        _class, _ = caseless_class
        caseless_dict: _class = _class()

        iterable = [(unhashable_type, 1)]

        with pytest.raises(TypeError):
            caseless_dict.update(iterable)
