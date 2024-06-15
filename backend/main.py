from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/tasks/{task_id}")
def read_task(task_id: int, q: str = None):
    return {"task_id": task_id, "q": q}
