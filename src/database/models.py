from typing import List
from datetime import datetime

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flask_sqlalchemy import SQLAlchemy



Base = declarative_base()
db = SQLAlchemy(model_class=Base, engine_options=dict(echo=True))


rev_prod_assoc = Table(
    "rev_prod_assoc",
    Base.metadata,
    Column("review_id", ForeignKey("reviews.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True )
)


class Review(Base):
    __tablename__ = "reviesws"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    text: Mapped[str] = mapped_column(String())


class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    name: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
    img_url: Mapped[str] = mapped_column(String())
    price: Mapped[float] = mapped_column()
    reviews: Mapped[List[Review]] = relationship(secondary=rev_prod_assoc)