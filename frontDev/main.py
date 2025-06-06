from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:2024/",
    "http://localhost:2024",
    "http://192.168.1.197:2024/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 定义数据模型（Pydantic）
class User(BaseModel):
    id: int
    name: str
    age: int

# 示例数据
users_db = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30}
]

# 1. 获取所有用户
@app.get("/api/users", response_model=List[User])
def get_users():
    return users_db

# 2. 获取单个用户
@app.get("/api/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 3. 创建用户
@app.post("/api/users", response_model=User, status_code=201)
def create_user(user: User):
    new_user = user.dict()
    new_user["id"] = len(users_db) + 1
    users_db.append(new_user)
    return new_user

# 4. 更新用户
@app.put("/api/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[index] = user.dict()
    return users_db[index]

# 5. 删除用户
@app.delete("/api/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    global users_db
    users_db = [u for u in users_db if u["id"] != user_id]
    return None