from fastapi import FastAPI, status
from database import db
from check import check_list
from typing import List, Dict


app = FastAPI()


@app.post('/api/v1/list', status_code=status.HTTP_201_CREATED)
async def main_post(items: Dict[str, List[int]]):
    for item in items.items():
        items_list = item[1]
        title = item[0]
        list_status = check_list(items_list)
        db[title] = list_status

    return db


@app.get('/api/v1/list', status_code=status.HTTP_200_OK)
async def main_fetch():
    return db
