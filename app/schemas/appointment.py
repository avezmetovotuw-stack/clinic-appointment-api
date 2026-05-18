from datetime import datetime
from pydantic import BaseModel, Field
from app.models.appointment import AppointmentStatus


class AppointmentCreate(BaseModel):
    doctor_id: int
    appointment_time: datetime
    reason: str | None = Field(default=None, max_length=500)


class AppointmentStatusUpdate(BaseModel):
    status: AppointmentStatus


class AppointmentOut(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_time: datetime
    reason: str | None
    status: str

    model_config = {"from_attributes": True}
