from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    address_item = relationship("AddressItem", back_populates="owner")



class AddressItem(Base):
    __tablename__ = "address_items"

    id = Column(Integer, primary_key=True)
    address = Column(String, index=True)
    lat = Column(Float, index=True)
    lon = Column(Float, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="address_item")