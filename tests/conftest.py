from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app import schemas, crud
from sqlalchemy.exc import IntegrityError
from types import SimpleNamespace

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # temporary in-memory DB

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

@fixture
def db_session():
    Base.metadata.create_all(bind=engine)   # create tables
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)     # clean up after each test

@fixture
def product_factory(db_session):
    def _create(**custom_fields):
        default_fields = {
            "name": "iPhone 15",
            "category": "Smartphones",
            "min_price": 1000.0,
            "url": "sdkjdfldkjlk"
        }
        default_fields.update(custom_fields)
        payload = schemas.ProductCreate(**default_fields)
        return crud.create_product(db_session, payload)
    return _create

def make_integrity_err(pgcode="23505"):
    # создаём объект orig с атрибутом pgcode, как у Postgres
    orig = SimpleNamespace(pgcode=pgcode)
    # IntegrityError(statement, params, orig)
    return IntegrityError("unique violation", params=None, orig=orig)