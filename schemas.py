from pydantic import BaseModel, ConfigDict
from typing import Optional



class AddressBase(BaseModel):
    address: str
    lat: float | None = None
    lon: float | None = None


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class AddressLatLon(BaseModel):
    address: Optional[str] 
    id: Optional[int]
    owner_id: Optional[int]
    lat: float | None = None
    lon: float | None = None
    
    class Config:
        orm_mode = True
    


class UserBase(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None



class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    is_active: bool
    address_item: list[Address] = []

    class Config:
        from_attributes = True
