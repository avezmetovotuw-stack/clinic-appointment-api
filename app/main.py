from fastapi import FastAPI

from app.api.routes import appointments, auth, doctors
from app.core.config import settings
from app.db.session import Base, engine
from app.models import Appointment, Doctor, User  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="Clinic Appointment API: doctors, patients, booking, JWT auth, CRUD, deployment-ready.",
    version="1.0.0",
)


@app.get("/", summary="Root / Bosh sahifa")
def root():
    return {"message": "Clinic Appointment API is running"}


@app.get("/health", summary="Health Check / Server holatini tekshirish")
def health():
    return {"status": "healthy"}


app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
