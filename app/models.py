from sqlalchemy import  Column, Integer, String, Numeric, TIMESTAMP, func
from .database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    name = Column(String)
    category = Column(String)
    min_price = Column(Numeric(12, 2))
    max_price= Column(Numeric(12,2))
    rating = Column(Numeric(2, 1))
    reviews_count = Column(Integer, default=0)
    scraped_at = Column(TIMESTAMP, server_default=func.now())