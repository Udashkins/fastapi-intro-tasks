from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str = Field(..., description="Размер продукта (например, 'M', 'L', 'XL')")
    color: str = Field(..., description="Цвет продукта")
    material: str = Field(..., description="Материал, из которого сделан продукт")


class Product(BaseModel):
    name: str = Field(..., description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта должна быть больше 0")
    specifications: ProductSpecifications


class ProductInDB(Product):
    id: int


@app.post("/product")
async def create_product(product: Product):
    global product_id_counter
    
    if product.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Цена должна быть больше 0"
        )
    
    # Создаем продукт с ID
    product_with_id = ProductInDB(
        id=product_id_counter,
        **product.dict()
    )
    
    # Добавляем в список
    product_list.append(product_with_id)
    
    # Увеличиваем счетчик ID
    product_id_counter += 1
    
    return {
        "message": "Product added successfully",
        "product": product_with_id.dict()
    }


@app.get("/products")
async def get_products():
    return {"products": [product.dict() for product in product_list]}

# END
