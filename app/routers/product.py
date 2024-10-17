from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import select, asc, desc
from app.db import get_db
from app.models.product import Product

router = APIRouter()

@router.get("/products")
def index(page: int = 1, size: int = 10, order = "id", direction = "asc", db: Session = Depends(get_db)):
    sort_direction = asc if direction == "asc" else desc
    products = (
        db.query(Product)
        .order_by(sort_direction(getattr(Product, order)))
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )
    return products