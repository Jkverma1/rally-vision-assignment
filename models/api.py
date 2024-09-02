from pydantic import BaseModel

class PersonDetectionRequest(BaseModel):
    input_url: str

class PersonDetectionResponse(BaseModel):
    task_id: str
