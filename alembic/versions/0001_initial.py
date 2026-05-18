"""initial tables

Revision ID: 0001_initial
Revises: 
Create Date: 2026-05-18
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0001_initial"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)

    op.create_table(
        "doctors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(length=100), nullable=False),
        sa.Column("specialization", sa.String(length=100), nullable=False),
        sa.Column("experience_years", sa.Integer(), nullable=False),
        sa.Column("phone", sa.String(length=30), nullable=False),
        sa.Column("room_number", sa.String(length=30), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_doctors_id"), "doctors", ["id"], unique=False)

    op.create_table(
        "appointments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("patient_id", sa.Integer(), nullable=False),
        sa.Column("doctor_id", sa.Integer(), nullable=False),
        sa.Column("appointment_time", sa.DateTime(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.ForeignKeyConstraint(["doctor_id"], ["doctors.id"]),
        sa.ForeignKeyConstraint(["patient_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_appointments_id"), "appointments", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_appointments_id"), table_name="appointments")
    op.drop_table("appointments")
    op.drop_index(op.f("ix_doctors_id"), table_name="doctors")
    op.drop_table("doctors")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
