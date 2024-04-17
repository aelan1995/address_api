from fastapi import Depends,  APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Depends
import models, schemas
from database import SessionLocal, engine

from typing import Optional, Annotated


models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/address/{lat}")
def get_address(db: Session = Depends(get_db)):
    return db.query(models.AddressItem).all()

@router.post("/address/{lat}&{lon}", response_model=schemas.Address)
def get_address_for_user(lat: float, lon: float, db: Session = Depends(get_db)):
    return db.query(models.AddressItem).filter(models.AddressItem.lat == lat).all()



@router.post("/address/{user_id}/", response_model=schemas.Address)
def create_address_for_user(
    user_id: int, address_item: schemas.AddressCreate, db: Session = Depends(get_db)
):
    db_item = models.AddressItem(**address_item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item