from fastapi import Depends,  APIRouter, Request
from sqlalchemy.orm import Session
from fastapi.params import Depends
import models, schemas
from sqlalchemy import and_
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Filter Relative Address
@router.post("/address/")
async def get_address_for_user(request: Request, lat: float, lon: float, db: Session = Depends(get_db)):
    get_filter = db.query(models.AddressItem).filter(and_(models.AddressItem.lat.contains == lat,models.AddressItem.lon.contains == lon)).all()
    if not get_filter:
       print(get_filter)
       
       return db.query(models.AddressItem).all()
    print('true')
    return get_filter


# Create (CREATE)
@router.post("/address/{user_id}/", response_model=schemas.Address)
def create_address_for_user(
    user_id: int, address_item: schemas.AddressCreate, db: Session = Depends(get_db)
):
    db_item = models.AddressItem(**address_item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Update (UPDATE)
@router.put("/address/{address_id}")
def update_address_for_user(address_id: int, address: str, lat: float, lon: float, db: Session = Depends(get_db)):
    db_item = db.query(models.AddressItem).filter(models.AddressItem.id == address_id).first()
    db_item.address = address
    db_item.lat = lat
    db_item.lon = lon
    db.commit()
    return db_item

# Delete (DELETE)
@router.delete("/address/{address_id}")
async def delete_address_for_user(address_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.AddressItem).filter(models.AddressItem.id == address_id).first()
    db.delete(db_item)
    db.commit()
    return {"message": "Address deleted successfully"}