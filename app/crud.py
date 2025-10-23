from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import select
from app.models import Product
from app import schemas
from app.exceptions import ProductAlreadyExists, DatabaseError



def get_product(db: Session, id: int):
    stmt = select(Product).where(Product.id == id)
    return db.scalar(stmt)

def get_products(db: Session):
    stmt = select(Product)
    return db.scalars(stmt).all()


def create_product(db: Session, product: schemas.ProductCreate):
    new_product = Product(**product.model_dump())
    db.add(new_product)
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        orig = getattr(e, "orig", None)
        pgcode = getattr(orig, "pgcode", None)
        if pgcode == "23505":
            raise ProductAlreadyExists("Product with this url already exists.")
        raise DatabaseError(f"Integrity error: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))

    db.refresh(new_product)
    return new_product

def delete_product(db: Session, id: int):
    product = db.get(Product, id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product


def update_product(db: Session, id: int, product_data: schemas.ProductCreate):
    product = db.get(Product, id)
    if not product:
        return None

    for key, value in product_data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product

if __name__ == '__main__':
    pass