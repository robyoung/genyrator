import factory

from bookshop.sqlalchemy import db
from bookshop.sqlalchemy.model.Review import Review


class ReviewFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Review
        sqlalchemy_session = db.session

    review_id = factory.Faker('uuid4', cast_to=lambda x: x)
    text = factory.Faker('pystr')
