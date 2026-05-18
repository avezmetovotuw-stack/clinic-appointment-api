from pydantic import BaseModel, Field
from app.schemas.appointment import AppointmentOut


class DoctorBase(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    specialization: str = Field(min_length=2, max_length=100)
    experience_years: int = Field(ge=0, le=70)
    phone: str = Field(min_length=5, max_length=30)
    room_number: str = Field(min_length=1, max_length=30)
    description: str | None = None


class DoctorCreate(DoctorBase):
    pass


class DoctorUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=2, max_length=100)
    specialization: str | None = Field(default=None, min_length=2, max_length=100)
    experience_years: int | None = Field(default=None, ge=0, le=70)
    phone: str | None = Field(default=None, min_length=5, max_length=30)
    room_number: str | None = Field(default=None, min_length=1, max_length=30)
    description: str | None = None


class DoctorOut(DoctorBase):
    id: int

    model_config = {"from_attributes": True}


class DoctorDetail(DoctorOut):
    appointments: list[AppointmentOut] = []
