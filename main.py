from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Read CSV data once at startup
students_data = []
with open("students.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["studentId"] = int(row["studentId"])  # Convert to int
        students_data.append(row)

@app.get("/api")
def get_students(class_: list[str] = Query(default=[])):
    if class_:
        filtered = [s for s in students_data if s["class"] in class_]
        return {"students": filtered}
    return {"students": students_data}
