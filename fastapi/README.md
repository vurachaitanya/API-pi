### FAST API 
- [Fast api to nginx redirection with SSL](https://lcalcagni.medium.com/deploy-your-fastapi-to-aws-ec2-using-nginx-aa8aa0d85ec7)
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
- `uvicorn <Filename>:app --reload` - Reload the webpage

### PATH Based
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

```
- `uvicorn <Filename>:app --reload` - Reload the webpage
- `curl http://127.0.0.1:8000/items/123` - test


### Base on URL 
```
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```
- `uvicorn <Filename>:app --reload` - Reload the webpage
- `curl http://127.0.0.1:8000/models/resnet` - test

### Switch ON & OFF:

```
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    ON = "ON"
    OFF = "OFF"
    status = "status"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.ON:
        return {"model_name": model_name, "message": "Switch is on"}

    if model_name.value == "OFF":
        return {"model_name": model_name, "message": "Switch is off"}

    return {"model_name": model_name, "message": "status of the switch"}

```
- `uvicorn <Filename>:app --reload` - Reload the webpage
- `curl http://127.0.0.1:8000/models/ON` - test


### Request and post 
```

from typing import List, Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
```
- `uvicorn <Filename>:app --reload` - Reload the webpage
- `curl http://127.0.0.1:8000/items/foo` - test
- POST : `curl -d '{"name": "chaitu", "description": "test of api"}' -X POST http://localhost:8000/items/bar/` **Notworking**
