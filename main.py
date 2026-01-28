from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import SessionLocal, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=['*'])

database_models.Base.metadata.create_all(bind=engine)

products = [
    Product(id=1, name="phone", description="Budger Phone", price=99, quantity=10),
    Product(
        id=2, name="laptop", description="Lightweight laptop", price=799, quantity=5
    ),
    Product(
        id=3,
        name="headphones",
        description="Wireless headphones",
        price=49,
        quantity=20,
    ),
    Product(
        id=4,
        name="smartwatch",
        description="Fitness tracking watch",
        price=129,
        quantity=15,
    ),
    Product(
        id=5, name="tablet", description="10-inch Android tablet", price=199, quantity=8
    ),
    Product(
        id=6, name="keyboard", description="Mechanical keyboard", price=69, quantity=25
    ),
    Product(id=7, name="mouse", description="Wireless mouse", price=29, quantity=30),
    Product(
        id=8, name="monitor", description="24-inch LED monitor", price=159, quantity=12
    ),
    Product(
        id=9, name="powerbank", description="10000mAh power bank", price=39, quantity=18
    ),
    Product(
        id=12,
        name="earbuds",
        description="Noise cancelling earbuds",
        price=59,
        quantity=22,
    ),
    Product(
        id=14, name="speaker", description="Bluetooth speaker", price=89, quantity=10
    ),
    Product(
        id=15,
        name="charger",
        description="Fast charging adapter",
        price=19,
        quantity=40,
    ),
    Product(
        id=18, name="usb_cable", description="Type-C USB cable", price=9, quantity=50
    ),
    Product(
        id=20,
        name="camera",
        description="Digital compact camera",
        price=299,
        quantity=6,
    ),
    Product(
        id=21, name="router", description="Dual band WiFi router", price=99, quantity=14
    ),
]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()

    count = db.query(database_models.Product).count

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

        db.commit()


init_db()


@app.get("/")
def greet():
    return "Wellcome to first FastApi Application.. yoyo"


@app.get("/products")
def get__all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()

    return db_products


@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if db_product:
        return db_product

    return "Product not found"


@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product Updated"
    else:
        return "Product not found"


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "Product not found"
