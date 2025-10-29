import pytest
from app.exceptions import ProductAlreadyExists, DatabaseError
from app import crud, schemas
from app.models import Product
from typing import Optional
from sqlalchemy.exc import IntegrityError
from tests.conftest import make_integrity_err

# def test_create_product(product_factory):
#     new_product = product_factory()
#
#     assert new_product.id is not None
#     assert new_product.name == "iPhone 15"
#
# def test_get_product(db_session, product_factory):
#     new_product = product_factory()
#     found = crud.get_product(db_session, new_product.id)
#     assert found.id == new_product.id
#
# def test_delete_product(db_session, product_factory):
#     new_product: Product = product_factory()
#     assert new_product.id is not None
#
#     # deleted_product — возвращаемое значение удаления (может быть ORM instance или None)
#     deleted_product: Optional[Product] = crud.delete_product(db_session, new_product.id)
#
#     # Проверяем, что удалённый объект — именно тот, что создали
#     assert deleted_product is not None
#     assert deleted_product.id == new_product.id
#
#     # get_product должен вернуть None после удаления
#     assert crud.get_product(db_session, new_product.id) is None


def test_create_product_duplicate_raises(monkeypatch, db_session, product_factory):
    def fake_commit():
        raise make_integrity_err("23505")

    monkeypatch.setattr(db_session, "commit", fake_commit)

    with pytest.raises(ProductAlreadyExists):
        product_factory()

# def test_delete_nonexistent_product(db_session):
#     deleted = crud.delete_product(db_session, 9999)
#     assert deleted is None
#
# def test_update_nonexistent_product(db_session):
#     data = schemas.ProductCreate(name="Ghost")
#     updated = crud.update_product(db_session, 9999, data)
#     assert updated is None
#
# def test_get_products_empty(db_session):
#     products = crud.get_products(db_session)
#     assert products == []
#
#
# def test_update_partial_fields(db_session, product_factory):
#     created = product_factory()
#
#     update_data = schemas.ProductCreate(name="Updated Phone")
#
#     updated = crud.update_product(db_session, created.id, update_data)
#
#     assert updated.name == "Updated Phone"
#     assert updated.url == "https://kaspi.kz/item"  # unchanged
#
# def test_create_product_with_nullables(db):
#     product_data = schemas.ProductCreate(name="Null Test", category=None, rating=None)
#     new_product = crud.create_product(db, product_data)
#     assert new_product is not None
#
#
# def test_create_product_integrity_error(monkeypatch, db_session):
#     def broken_commit():
#         raise IntegrityError("fake", "fake", "fake")
#     monkeypatch.setattr(db_session, "commit", broken_commit)
#
#     data = schemas.ProductCreate(name="Test", url="https://kaspi.kz/item")
#     result = crud.create_product(db_session, data)
#     assert result is None
