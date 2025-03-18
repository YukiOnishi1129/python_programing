from fastapi import FastAPI

app = FastAPI()

# Get
@app.get("/")
async def get_hello():
    return {"message": "Hello World"}