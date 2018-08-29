from typing import Any, Mapping, Union, List

from bookshop.core.convert_case import to_json_name
from bookshop.domain.types import DomainModel


def create_joined_entity_map(
    domain_model: DomainModel,
    data:         Mapping[str, Any]
) -> Union[List[str], Mapping[str, Any]]:
    errors = []
    joined_entities = {}
    for relationship_name, relationship in domain_model.relationship_map.items():
        json_relationship_name = to_json_name(relationship_name)
        if json_relationship_name not in data:
            continue
        target_identifier_value = data[json_relationship_name]
        filter_kwargs = {relationship.target_identifier_column: target_identifier_value}
        result = relationship.target.query.filter_by(**filter_kwargs).first()
        if result is None:
            errors.append(
                [f'Could not find {relationship.target_name} with {json_relationship_name} equal to {target_identifier_value}']
            )
        else:
            joined_entities[relationship_name] = result
    return errors if errors else joined_entities