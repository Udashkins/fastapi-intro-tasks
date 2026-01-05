from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Product(BaseModel):
    name: str = Field(..., min_length=1, description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта (должна быть больше нуля)")
    quantity: int = Field(..., ge=0, description="Количество продукта на складе (должно быть >= 0)")


# Модель для ответа с ID (используется в GET-запросе)
class ProductResponse(Product):
    id: int


@app.post("/product")
async def add_product(product: Product):
    """
    Добавление нового продукта в базу данных
    """
    global product_id_counter
    
    # Создаем словарь с данными продукта
    product_data = product.dict()
    product_data["id"] = product_id_counter
    
    # Добавляем продукт в список
    product_list.append(product_data)
    
    # Увеличиваем счетчик ID
    product_id_counter += 1
    
    # Возвращаем продукт с id в ответе (как ожидается в тестах)
    return {
        "message": "Product added successfully",
        "product": product_data
    }


@app.get("/products")
async def get_products():
    """
    Получение списка всех продуктов
    """
    # Возвращаем объект с полем products (как ожидается в тестах)
    return {"products": product_list}

# END
