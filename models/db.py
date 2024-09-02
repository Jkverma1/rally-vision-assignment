from pydantic import BaseModel

class DetectionJob(BaseModel):
    task_id: str
    input_url: str
    result: dict
