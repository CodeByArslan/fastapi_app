from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Item
@router.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    item = models.Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

# Get Items
@router.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()
