from pydantic import BaseModel


class Item(BaseModel):
	item_id: str
	description: str
