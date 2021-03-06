from datetime import datetime, date
from enum import Enum
from typing import Any, Optional
from uuid import UUID


class TypeOption(Enum):
    string =   'string'
    int =      'int'
    float =    'float'
    bool =     'bool'
    dict =     'dict'
    list =     'list'
    datetime = 'datetime'
    date =     'date'
    UUID =     'UUID'


def string_to_type_option(string_type: str) -> TypeOption:
    return {
        'str':      TypeOption.string,
        'int':      TypeOption.int,
        'float':    TypeOption.float,
        'bool':     TypeOption.bool,
        'dict':     TypeOption.dict,
        'list':     TypeOption.list,
        'datetime': TypeOption.datetime,
        'date':     TypeOption.date,
        'UUID':     TypeOption.UUID,
    }[string_type]


def python_type_to_type_option(python_type: Any) -> TypeOption:
    return {
        str:      TypeOption.string,
        int:      TypeOption.int,
        float:    TypeOption.float,
        bool:     TypeOption.bool,
        dict:     TypeOption.dict,
        list:     TypeOption.list,
        datetime: TypeOption.datetime,
        date:     TypeOption.date,
        UUID:     TypeOption.UUID,
    }[python_type]


def type_option_to_type_constructor(type_option: TypeOption):
    return {
        TypeOption.string:   str,
        TypeOption.int:      int,
        TypeOption.float:    float,
        TypeOption.bool:     bool,
        TypeOption.dict:     dict,
        TypeOption.list:     list,
        TypeOption.datetime: str,
        TypeOption.date:     str,
        TypeOption.UUID:     str,
    }[type_option]


class SqlAlchemyTypeOption(Enum):
    string =   'db.String'
    float =    'db.Float'
    int =      'db.BigInteger'
    bool =     'db.Boolean'
    datetime = 'db.DateTime'
    date =     'db.Date'
    UUID =     'UUIDType'
    dict =     'JSONType'


class RestplusTypeOption(Enum):
    string =   'String'
    float =    'Float'
    int =      'Integer'
    bool =     'Boolean'
    datetime = 'DateTime'
    date =     'Date'
    UUID =     'String'
    dict =     'Raw'


def type_option_to_sqlalchemy_type(type_option: TypeOption) -> SqlAlchemyTypeOption:
    return getattr(SqlAlchemyTypeOption, type_option.value)


def type_option_to_restplus_type(type_option: TypeOption) -> RestplusTypeOption:
    return getattr(RestplusTypeOption, type_option.value)


class PythonTypeOption(Enum):
    string =   'str'
    float =    'float'
    int =      'int'
    bool =     'bool'
    dict =     'Dict'
    list =     'List'
    datetime = 'datetime'
    date =     'date'
    UUID =     'UUID'


def type_option_to_python_type(type_option: TypeOption) -> PythonTypeOption:
    return getattr(PythonTypeOption, type_option.value)


def type_option_to_default_value(type_option: TypeOption) -> str:
    return {
        TypeOption.string:   '""',
        TypeOption.float:    '0.0',
        TypeOption.int:      '0',
        TypeOption.bool:     'None',
        TypeOption.dict:     '{}',
        TypeOption.list:     '[]',
        TypeOption.datetime: '"1970-01-01T00:00"',
        TypeOption.date:     '"1970-01-01T00:00"',
        TypeOption.UUID:     '"00000000-0000-0000-0000-000000000000"',
    }[type_option]


def type_option_to_faker_method(type_option: TypeOption) -> str:
    return {
        TypeOption.string:   'pystr',
        TypeOption.float:    'pyfloat',
        TypeOption.int:      'pyint',
        TypeOption.bool:     'pybool',
        TypeOption.dict:     'pydict',
        TypeOption.list:     'pylist',
        TypeOption.datetime: 'date_time_this_decade',
        TypeOption.date:     'date_this_year',
        TypeOption.UUID:     'uuid4',
    }[type_option]


def type_option_to_faker_options(type_option: TypeOption) -> Optional[str]:
    if type_option == TypeOption.UUID:
        return 'cast_to=lambda x: x'
    else:
        return None
