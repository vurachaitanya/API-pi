### FAST API 

- [FAST API Source](https://fastapi.tiangolo.com/tutorial/)
- `pip install fastapi` - install Fast api
- `pip install "uvicorn[standard]"` - Install Webapp to support fastapi
- Test hello world api deploy
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
`uvicorn <Filename>:app --reload` - Reload the webpage

### PATH Based
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

```
`uvicorn <Filename>:app --reload` - Reload the webpage
`curl http://127.0.0.1:8000/items/123` - test
