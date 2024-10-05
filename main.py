from enum import Enum

from fastapi import FastAPI

from .models import Item

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}

items = [
	"hello",
	"world",
	"here",
	"im",
	"once",
	"again",
	"saying",
	"that",
	"obladi",
	"oblada",
	"I",
	"need",
	"more",
	"words",
	"and",
	"done",
]

@app.get("/search/")
async def search(q: str):
	return {"results": []}

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10, q: str | None = None):

	if q:
		return [item for item in items if q in item]

	return items[skip:skip+limit]

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/{item_id}/attributes")
async def read_item_attributes(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def read_model(model_name: ModelName):

	res = {"model_name": model_name}
	
	if model_name is ModelName.alexnet:
		return {**res, "message": "Deep learning FTW!"}
	
	if model_name is ModelName.resnet:
		return {**res, "message": "LeCNN all the images"} 

	return {**res, "message": "Have some residuals"}

@app.get("/file/{file_path:path}")
async def read_file(file_path: str):
	return {"file_path": file_path}

@app.post("/items/")
async def create_item(item: Item):
	items.append(item)
	return {"success": True}

