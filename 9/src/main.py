from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Specifications(BaseModel):
    size: str = Field(..., description="Размер продукта")
    color: str = Field(..., description="Цвет продукта")
    material: str = Field(..., description="Материал продукта")

class Product(BaseModel):
    name: str = Field(..., min_length=1, description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта (должна быть больше 0)")
    specifications: Specifications

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class ProductDetailResponse(BaseModel):
    id: int
    name: str
    price: float
    specifications: Specifications

@app.post("/product")
async def create_product(product: Product):
    global product_id_counter, product_list
    product_data = product.dict()
    product_data["id"] = product_id_counter
    product_list.append(product_data)
    product_id_counter += 1
    return product_data  # Возвращаем полные данные продукта

@app.get("/products", response_model=List[ProductResponse])
async def get_products():
    return product_list

@app.get("/product/{product_id}", response_model=ProductDetailResponse)
async def get_product(product_id: int):
    for product in product_list:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# END