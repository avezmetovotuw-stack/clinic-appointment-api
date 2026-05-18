from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    specialization: Mapped[str] = mapped_column(String(100), nullable=False)
    experience_years: Mapped[int] = mapped_column(Integer, default=0)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)
    room_number: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    appointments = relationship("Appointment", back_populates="doctor", cascade="all, delete-orphan")
