from pydentatic import BaseSettings, Field, validator 
form bson.objectid import ObjectId
class DataChunk(BaseModel): 
    _id: optional[ObjectId]
    Chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId


    class config:
        arbitrary_types_allowed = True
         