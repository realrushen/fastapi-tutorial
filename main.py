from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_40)
async def create_item(name: str):
    return {"name": name}