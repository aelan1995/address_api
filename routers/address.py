from fastapi import Depends,  APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Depends
import models, schemas
from database import SessionLocal, engine

from typing import Optional, Annotated
from fastapi_filter.contrib.sqlalchemy import Filter

class UserFilter(Filter):
    order_by: Optional[list[str]]



models.Base.metadata.create_all(bind=engine)



router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/address/")
def get_address(db: Session):
    current_user: Annotated[schemas.UserBase, Depends(get_current_active_user)],
    return db.query(models.AddressItem).all()


@router.post("/users/{user_id}/address/", response_model=schemas.Address)
def create_address_for_user(
    user_id: int, address_item: schemas.AddressCreate, db: Session = Depends(get_db)
):
    db_item = models.AddressItem(**address_item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item