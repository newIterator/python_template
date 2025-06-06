# use the python to write front API

## one、create env

> first、 the moused move on target folder,click right key or use two fingers click laptops control block,when the selects show,select create new terminal
>
> second、cd your project folder
>
> three、init your project folder
```
python3 -m venv venv  
```

> four、 install need dependence of package in the venv
```
pip uninstall fastapi uvicorn

```

> five、create the .py file to write needs of front dev API
>> first、create the file of name is "main.py "

>> second、start write
```
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()
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
```
>
> finish、check the result, input the command on the terminal
```
uvicorn main:app --reload
```

# answer the cors question
> first、import CORSMiddleware methods into main.py from "fastapi.middleware.cors"
>
> second、write the about config, open the main.py

``` other code watch up example of main.py
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:2024/",
    "http://localhost:2024",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
# Fastapi

> [fastapi官方地址](https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-hero)


