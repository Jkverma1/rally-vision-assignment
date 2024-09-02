from fastapi import FastAPI, HTTPException
from models.api import PersonDetectionRequest, PersonDetectionResponse
from services.person_detection_service import PersonDetectionService
from models.db import DetectionJob
from uuid import uuid4

app = FastAPI()
service = PersonDetectionService(model_weights_url='your_model_weights_url_here')

jobs = {}

@app.post("/detect-person", response_model=PersonDetectionResponse)
async def detect_person(request: PersonDetectionRequest):
    task_id = str(uuid4())
    result = service.detect_person(request.input_url)
    jobs[task_id] = DetectionJob(task_id=task_id, input_url=request.input_url, result=result)
    return PersonDetectionResponse(task_id=task_id)

@app.get("/result/{task_id}")
async def get_result(task_id: str):
    job = jobs.get(task_id)
    if job:
        return job
    raise HTTPException(status_code=404, detail="Task not found")
