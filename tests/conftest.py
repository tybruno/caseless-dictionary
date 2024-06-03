from typing import Mapping, Any, Callable, Hashable, NamedTuple, Type, Union

import pytest

from caseless_dictionary import SnakeCaselessAttrDict, \
    ConstantCaselessAttrDict, CaselessAttrDict, KebabCaselessDict, \
    CaselessDict, ConstantCaselessDict, UpperCaselessDict, SnakeCaselessDict, \
    TitleCaselessDict


class _TestingClass(NamedTuple):
    cls: Union[
        Type[CaselessDict],
        Type[CaselessAttrDict],
    ]
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


def _lower(value: Any):
    if isinstance(value, str):
        value = value.strip().lower()
    return value


def _snake_case(value: Any):
    if isinstance(value, str):
        value = value.strip().replace(' ', '_').casefold()
    return value


def _kebab_case(value: Any):
    if isinstance(value, str):
        value = value.strip().replace(' ', '-').casefold()
    return value


def _constant_case(value: Any):
    if isinstance(value, str):
        value = value.strip().replace(' ', '_').upper()
    return value


@pytest.fixture(
    params=(
        {
            'CamelCase': 1,
            'lower': 2,
            'UPPER': 3,
            'snake_case': 4,
            5.56: 'Five',
            True: 'True',
        },
        {1: 2, ('hello', 'Goodbye'): 2},
        {'kebab-case': 5, 'CONSTANT_CASE': 6, 'Title Case': 7},
        {False: 'False', 3.14: 'Pi', 'pascalCase': 8},
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
        _TestingClass(SnakeCaselessDict, _snake_case),
        _TestingClass(KebabCaselessDict, _kebab_case),
        _TestingClass(
            ConstantCaselessDict, _constant_case
        ),
    )
)
def caseless_class(request) -> _TestingClass:
    _caseless_class: _TestingClass = request.param
    return _caseless_class


@pytest.fixture(
    params=(
        _TestingClass(SnakeCaselessAttrDict, _snake_case),
        _TestingClass(
            ConstantCaselessAttrDict, _constant_case
        ),
    )
)
def caseless_attr_class(request) -> _TestingClass:
    _caseless_attr_class: _TestingClass = request.param
    return _caseless_attr_class


@pytest.fixture(params=(set(), list(), dict()))
def unhashable_type(request):
    unhashable_type = request.param
    return unhashable_type
