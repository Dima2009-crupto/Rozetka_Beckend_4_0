from uuid import uuid4
from typing import List

from src.database.models import db, Product, Review


def get_products():
    return db.session.query(Product).all()


def get_product(prod_id: str):
    return db.session.query(Product).where(Product.id == prod_id).first()


def add_products(
        name: str,
        descrition:str,
        img_url: str,
        price: float
)-> str:
    product = Product(
        id=uuid4().hex,
        name=name,
        descrition=descrition,
        img_url=img_url,
        price=price
    )
    db.session.add(product)
    db.session.commit()
    return product.id


def edit_product(
    prod_id: str,
    name: str,
    description: str,
    img_url: str,
    price: float
)->str:
    product = db.session.query(Product).where(Product.id == prod_id).first()
    product.name = name
    product.description = description
    product.img_url = img_url
    product.price = price
    db.session.commit()
    return "Successful"


def del_product(prod_id: str) -> str:
    product = db.session.query(Product).where(Product.id == prod_id).first()
    db.session.delete(product)
    db.session.commit()
    return "Successful"


def get_reviews() -> List[Review]:
    return db.session.query(Review).all()


def get_review(review_id: str) -> Review:
    return db.one_or_404(db.session.query(Review).where(Review.id == review_id))


def add_review(
    text: str,
    author: str,
    rating: float
) -> str:
    review = Review(
        id=uuid4().hex,
        text=text,
        author=author,
        rating=rating
    )
    db.session.add(review)
    db.session.commit()
    db.session.refresh(review)
    return review.id


def edit_review(
        rev_id: str,
        text: str,
        author: str,
        rating: float
) -> str:
    review = db.one_or_404(db.session.query(Review).where(Review.id == rev_id))
    review.text = text
    review.author = author
    review.rating = rating
    db.session.commit()
    return "Successful"


def del_review(rev_id: str) -> str:
    review = db.one_or_404(db.session.query(Review).where(Review.id == rev_id))
    db.session.delete(review)
    db.session.commit()
    return "Successful"