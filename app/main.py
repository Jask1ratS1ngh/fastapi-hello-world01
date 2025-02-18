import uvicorn
from fastapi import FastAPI 

app = FastAPI(
    title="FastAPI - Hello World",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
) 


@app.get("/")
def hello_world():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)
