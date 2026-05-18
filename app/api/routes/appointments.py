from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.user import User
from app.schemas.appointment import AppointmentCreate, AppointmentOut, AppointmentStatusUpdate

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("/", response_model=AppointmentOut, status_code=status.HTTP_201_CREATED, summary="Book Appointment / Qabulga yozilish")
def book_appointment(data: AppointmentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    doctor = db.query(Doctor).filter(Doctor.id == data.doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor topilmadi")

    appointment = Appointment(
        patient_id=current_user.id,
        doctor_id=data.doctor_id,
        appointment_time=data.appointment_time,
        reason=data.reason,
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment


@router.get("/", response_model=list[AppointmentOut], summary="List My Appointments / Mening appointmentlarim")
def list_my_appointments(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Appointment).filter(Appointment.patient_id == current_user.id).all()


@router.patch("/{appointment_id}/status", response_model=AppointmentOut, summary="Update Appointment Status / Appointment status update")
def update_status(appointment_id: int, data: AppointmentStatusUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment topilmadi")

    appointment.status = data.status.value
    db.commit()
    db.refresh(appointment)
    return appointment
