import datetime
import uuid
from typing import Mapping, Callable, Any, Iterable, List, Optional
from bookshop.core.convert_case import to_json_name, to_python_name
from bookshop.domain.types import UserJson


def convert_dict_naming(
    in_dict: Optional[Mapping[str, Any]],
    fn:      Callable[[str], str],
) -> Optional[Mapping[str, Any]]:
    if in_dict is None:
        return None
    out_dict = {}
    for k, v in in_dict.items():
        # don't change the casing of JSON which the user has supplied
        if type(v) is UserJson:
            value = v
        elif type(v) is dict:
            value = convert_dict_naming(v, fn)
        elif type(v) is list or type(v) is set:
            value = convert_iterable_naming(v, fn)
        else:
            value = dict_value_to_json_value(v, fn)
        out_dict[fn(k)] = dict_value_to_json_value(value, fn)
    return out_dict


def convert_iterable_naming(
    in_list: Iterable,
    fn:      Callable[[str], str],
) -> List:
    return [
        dict_value_to_json_value(value, fn) for value in in_list
    ]


def python_dict_to_json_dict(python_dict: Mapping[str, Any]) -> Mapping[str, Any]:
    return convert_dict_naming(python_dict, to_json_name)


def json_dict_to_python_dict(json_dict: Mapping[str, Any]) -> Mapping[str, Any]:
    return convert_dict_naming(json_dict, to_python_name)


def dict_value_to_json_value(param: Any, fn: Callable[[str], str]) -> Any:
    if isinstance(param, dict):
        return convert_dict_naming(param, fn)
    elif isinstance(param, (list, set)):
        return convert_iterable_naming(param, fn)
    elif isinstance(param, (datetime.datetime, datetime.date)):
        return param.isoformat()
    elif isinstance(param, uuid.UUID):
        return str(param)
    return param
