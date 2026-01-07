from constants import DATA_PATH
import json
from pprint import pprint
from pydantic import BaseModel, Field

def read_json(filename):
    with open(DATA_PATH / filename) as file:
        data = json.load(file)
    
    return data

class Book(BaseModel):
    id: int
    title: str
    year: int = Field(gt = 1000, lt=2027, description="Year when book was published")
    author: str
    description: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 11,
                "title": "Fluent Python",
                "year": 2022,
                "author": "Luciano Ramlho",
                "desription": "Deep dive into Python"
            }
        }
    }
    
class Library(BaseModel):
    name: str
    books: list[Book]

def library_data(filename):
    json_data = read_json(filename)
    return Library(**json_data)

if __name__ == "__main__":
    pprint(library_data("library.json"))