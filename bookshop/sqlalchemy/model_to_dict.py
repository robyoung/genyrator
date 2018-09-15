from typing import List, Mapping, Any, Optional

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList

from bookshop.core.convert_dict import python_dict_to_json_dict
from bookshop.sqlalchemy.convert_between_models import convert_sqlalchemy_model_to_domain_model


def model_to_dict(
    sqlalchemy_model: Optional[DeclarativeMeta],
    paths:            List[str] = list(),
) -> Optional[Mapping[str, Any]]:
    """
    recursively convert a sql alchemy result into a dictionary
    """
    if sqlalchemy_model is None:
        return None
    domain_model = convert_sqlalchemy_model_to_domain_model(sqlalchemy_model)
    serialized_data = {}
    for domain_property in domain_model.property_keys:
        if domain_property in domain_model.json_translation_map:
            dict_key = domain_model.json_translation_map[domain_property]
        else:
            dict_key = domain_property
        value = getattr(sqlalchemy_model, domain_property)
        serialized_data[dict_key] = value
    if not paths:
        return python_dict_to_json_dict(serialized_data)
    next_path = paths[0]
    next_relationship = getattr(sqlalchemy_model, next_path)
    next_key = next_path
    if type(next_relationship) is InstrumentedList:
        serialized_data[next_key] = [
            python_dict_to_json_dict(model_to_dict(
                sqlalchemy_model=nr,
                paths=paths[1:]
            ))
            for nr in next_relationship
        ]
    else:
        serialized_data[next_key] = python_dict_to_json_dict(
            model_to_dict(sqlalchemy_model=next_relationship, paths=paths[1:])
        )
    return python_dict_to_json_dict(serialized_data)
