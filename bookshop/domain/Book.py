from bookshop.domain.types import DomainModel, Relationship


from bookshop.sqlalchemy.model.Author import Author
from bookshop.sqlalchemy.model.Review import Review
from bookshop.sqlalchemy.model.Genre import Genre

book = DomainModel(
    external_identifier_map={
        'author_id': Relationship(
            sqlalchemy_model_class=Author,
            target_name='author',
            target_identifier_column='author_id',
            source_foreign_key_column='author_id',
            lazy=False,
            nullable=False,
        ),
    },
    identifier_column_name='book_id',
    relationship_keys=[
        'author',
        'reviews',
        'genre',
    ],
    property_keys=[
        'book_id',
        'name',
        'rating',
        'author_id',
        'published',
        'created',
    ],
    json_translation_map={
        'book_id': 'id',
        'author_id': 'author',
    },
    eager_relationships=[
        'author',
        'genre',
    ],
)
