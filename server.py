from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

@app.post("/detect-person")
async def detect_person(file: UploadFile = File(...)):
    file_location = f"temp/{file.filename}"
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    task_id = "some-task-id"  

    return {"task_id": task_id}

@app.get("/result/{task_id}")
async def get_result(task_id: str):
    if task_id == "some-task-id":
        return {"status": "success", "data": "Person detected"}
    else:
        return JSONResponse(status_code=404, content={"detail": "Not found"})
