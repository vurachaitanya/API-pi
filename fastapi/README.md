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
