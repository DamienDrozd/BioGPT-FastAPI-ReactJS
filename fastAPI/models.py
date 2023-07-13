from pydantic import BaseModel
from bson import ObjectId


class SentenceModel(BaseModel):
    note: str
    phrase: str

    class Config:
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}
        # schema_extra = {
        #     "note": "test",
        #     "phrase": "test de fastAPI"
        # }
