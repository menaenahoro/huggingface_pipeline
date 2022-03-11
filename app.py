from fastapi import FastAPI
from typing import List, Dict, Optional
from function import get_results


app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/search_word")
# ,since_date: Optional[datetime.date] = None, until_date: Optional[datetime.date] = None):
def read_item(list_item: List[str]):
    result = get_results(list_item)
    return {"result": result}
