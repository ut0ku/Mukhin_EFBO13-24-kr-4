from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, EmailStr
from pydantic.types import conint, constr
from typing import Optional

app = FastAPI()

users = {}

class ErrorResponse(BaseModel):
    detail: str

class CustomExceptionA(Exception):
    def __init__(self, message: str = "Custom Exception A occurred"):
        self.message = message
        self.status_code = 400
        super().__init__(self.message)

class CustomExceptionB(Exception):
    def __init__(self, message: str = "Custom Exception B occurred"):
        self.message = message
        self.status_code = 404
        super().__init__(self.message)

class User(BaseModel):
    username: str
    email: str
    age: int
    phone: Optional[str] = None

class UserValidation(BaseModel):
    username: str
    age: conint(gt=18)
    email: EmailStr
    password: constr(min_length=8, max_length=16)
    phone: Optional[str] = 'Unknown'

class User(BaseModel):
    username: str
    email: str
    age: int
    phone: Optional[str] = None

@app.exception_handler(CustomExceptionA)
async def custom_exception_a_handler(request: Request, exc: CustomExceptionA):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.exception_handler(CustomExceptionB)
async def custom_exception_b_handler(request: Request, exc: CustomExceptionB):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = ".".join(str(loc) for loc in error['loc'])
        msg = error['msg']
        errors.append(f"Field '{field}': {msg}")
    return JSONResponse(
        status_code=422,
        content={"detail": "Validation error", "errors": errors}
    )

@app.get("/trigger-a")
def trigger_a(value: int):
    if value < 0:
        raise CustomExceptionA("Value must be non-negative")
    return {"message": "Value is valid"}

@app.get("/trigger-b/{item_id}")
def trigger_b(item_id: int):
    if item_id == 999:
        raise CustomExceptionB("Item not found")
    return {"item_id": item_id, "message": "Item found"}

@app.post("/users")
def create_user(user: UserValidation):
    user_id = len(users) + 1
    users[user_id] = user.model_dump()
    return {"message": "User created", "user_id": user_id, "user": users[user_id]}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "user": users[user_id]}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted", "user_id": user_id}