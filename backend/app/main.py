from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Global backend status
# -----------------------------
backend_status = {
    "status": "Active",
    "name": None
}


# -----------------------------
# Request model
# -----------------------------
class BackendStatus(BaseModel):
    name: str
    status: str


# -----------------------------
# Temporary data
# -----------------------------
people = {
    "kiran": {
        "name": "Kiran Kumar",
        "role": "Robotics Engineer",
        "about": "I work on ROS2, AMR and robotics.",
        "skills": ["Python", "ROS2", "Angular", "Isaac Sim"]
    },

    "pavan": {
        "name": "Pavan Ashok Bushetti",
        "role": "Software Engineer",
        "about": "I develop applications of Opceneter",
        "skills": ["C#", "Angular", "JavaScript", "SQL"]
    }
}


# -----------------------------
# Check backend status
# -----------------------------
def check_backend_status():

    if backend_status["status"] != "Active":
        raise HTTPException(
            status_code=503,
            detail="Backend is currently deactivated"
        )


# -----------------------------
# Backend status API
# -----------------------------
@app.post("/api/backend-status")
async def update_backend_status(data: BackendStatus):

    backend_status["name"] = data.name
    backend_status["status"] = data.status

    return {
        "message": f"Backend status changed to {data.status}",
        "status": data.status
    }


# -----------------------------
# Person API
# -----------------------------
@app.get("/api/person/{person_id}")
def get_person(
    person_id: str,
    _: None = Depends(check_backend_status)
):

    person = people.get(person_id.lower())

    if person is None:
        raise HTTPException(
            status_code=404,
            detail="Person not found"
        )

    return person


# -----------------------------
# Example another API
# -----------------------------
@app.get("/api/people")
def get_people(
    _: None = Depends(check_backend_status)
):

    return people


# -----------------------------
# Start server
# -----------------------------
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )