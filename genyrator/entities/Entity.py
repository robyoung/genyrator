import attr
from typing import List, Optional, NewType, Union, Tuple, Dict

from genyrator.entities.Relationship import Relationship
from genyrator.entities.Column import Column, create_column
from genyrator.inflector import pythonize
from genyrator.types import string_to_type_option

Property = NewType('Property', Union[Column, Relationship])


@attr.s
class Entity(object):
    python_name:          str =                attr.ib()
    class_name:           str =                attr.ib()
    columns:              List[Column] =       attr.ib()
    relationships:        List[Relationship] = attr.ib()
    table_name:           Optional[str] =      attr.ib()
    uniques:              List[List[str]] =    attr.ib()
    properties:           List[Property] =     attr.ib()
    max_property_length:  int =                attr.ib()


def create_entity(
        class_name:    str,
        columns:       List[Column],
        relationships: List[Relationship] = list(),
        table_name:    Optional[str]=None,
        uniques:       List[List[str]]=list(),
) -> Entity:
    properties: List[Property] = columns + relationships
    return Entity(
        class_name=class_name,
        python_name=pythonize(class_name),
        columns=columns,
        max_property_length=(max(*[len(x.python_name) for x in properties])),
        relationships=relationships,
        table_name=table_name if table_name else None,
        uniques=uniques,
        properties=properties
    )


def create_entity_from_type_dict(
        class_name:    str,
        type_dict:     Dict,
        foreign_keys:  List[Tuple[str, str]]=list(),
        indexes:       List[str]=list(),
        relationships: Optional[List[Relationship]] = list(),
        table_name:    Optional[str]=None,
        uniques:       Optional[List[List[str]]]=list()
) -> Entity:
    columns = []
    foreign_keys_dict = {}
    for fk_key, fk_value in foreign_keys:
        foreign_keys_dict[fk_key] = '{table}.{fk_column}'.format(
            table=fk_value, fk_column=pythonize(fk_key)
        )
    for k, v in type_dict.items():
        type_option = string_to_type_option(v)
        foreign_key = foreign_keys_dict[k] if k in foreign_keys_dict else None
        index = k in indexes
        columns.append(
            create_column(k, type_option, foreign_key, index)
        )
    return create_entity(
        class_name=class_name,
        columns=columns,
        relationships=relationships,
        table_name=table_name,
        uniques=uniques,
    )