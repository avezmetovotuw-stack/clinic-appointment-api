from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.doctor import Doctor
from app.models.user import User
from app.schemas.doctor import DoctorCreate, DoctorDetail, DoctorOut, DoctorUpdate

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.post("/", response_model=DoctorOut, status_code=status.HTTP_201_CREATED, summary="Add Doctor / Doctor qo‘shish")
def create_doctor(data: DoctorCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    doctor = Doctor(**data.model_dump())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


@router.get("/", response_model=list[DoctorOut], summary="List Doctors / Doctorlar ro‘yxati")
def list_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()


@router.get("/{doctor_id}", response_model=DoctorDetail, summary="Doctor Detail / Doctor detail ichida appointmentlar")
def doctor_detail(doctor_id: int, db: Session = Depends(get_db)):
    doctor = (
        db.query(Doctor)
        .options(joinedload(Doctor.appointments))
        .filter(Doctor.id == doctor_id)
        .first()
    )
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor topilmadi")
    return doctor


@router.put("/{doctor_id}", response_model=DoctorOut, summary="Edit Doctor / Doctorni tahrirlash")
def update_doctor(doctor_id: int, data: DoctorUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor topilmadi")

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(doctor, key, value)

    db.commit()
    db.refresh(doctor)
    return doctor


@router.delete("/{doctor_id}", summary="Delete Doctor / Doctorni o‘chirish")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor topilmadi")

    db.delete(doctor)
    db.commit()
    return {"message": "Doctor muvaffaqiyatli o‘chirildi", "doctor_id": doctor_id}
