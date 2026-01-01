from fastapi import FastAPI
from models import Product
app = FastAPI()


@app.get("/")
def greet():
    return "Welcome to Baradol"


products = [
    Product(id=1, name="IQOO 15", description="IQOO 15 is a smartphone with 10000mAh battery",
            price=10000, quantity=100),
    Product(id=2, name="IQOO 15 Pro",
            description="IQOO 15 Pro is a smartphone with 10000mAh battery", price=15000, quantity=100),
    Product(id=3, name="ASUS ROG Strix G15",
            description="ASUS ROG Strix G15 is a gaming laptop with 10000mAh battery", price=20000, quantity=100),
]


@app.get("/products")
def get_all_products():
    return products


@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product


@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"
    return "Product not found"
