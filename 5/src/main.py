from fastapi import FastAPI, Body
from typing import Optional

app = FastAPI()

# BEGIN (write your solution here)
@app.post("/users")
def create_user(
    username: str = Body(..., embed=True),
    email: str = Body(..., embed=True),
    age: Optional[int] = Body(None, embed=True)
):
    return {
        "username": username,
        "email": email,
        "age": age,
        "status": "User created"
    }
# END
