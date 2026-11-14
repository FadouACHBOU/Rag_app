from pydentatic import BaseSettings, Field, validator
from typing import optional
from bson.objectid import ObjectId

class Project(BaseModel): 
    -id: optional[ObjectId]
    project-id: str = Field(..., min_length=1)
    @validator('project-id') 
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError('Project ID must be alphanumeric')
        return value

    class config:
        arbitrary_types_allowed = True
         