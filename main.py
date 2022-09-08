from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    name: str
    last_name: str


class Lists(BaseModel):
    lists: List[int]
    status: Optional[bool]


app = FastAPI()

db: List[Lists] = [

]


@app.post('/')
async def main_post(item: Lists):
    items_list = item.lists
    items_length = len(items_list)
    unique_length = len(set(items_list))
    sorted_list = sorted(items_list)
    if items_length == unique_length and sorted_list[0] == 0 and sorted_list[(items_length - 1)] == (items_length - 1):
        item.status = True

    else:
        item.status = False

    db.append(item)
    return db


@app.get('/')
async def fetch():
    return db
