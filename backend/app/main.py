from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Temporary data
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


@app.get("/api/person/{person_id}")
def get_person(person_id: str):

    person = people.get(person_id)

    if person is None:
        raise HTTPException(
            status_code=404,
            detail="Person not found"
        )

    return person


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )