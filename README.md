# Clinic Appointment API

Temirov Og‘abek — FastAPI clinic appointment backend.

## Vazifasi

Bu loyiha doctorlar va patient appointmentlarini boshqaradi. Patient ro‘yxatdan o‘tadi, login qiladi, doctor qabuliga yoziladi va appointment statuslari boshqariladi.

## Texnologiyalar

- FastAPI
- SQLAlchemy ORM
- Alembic migration
- JWT Authentication
- SQLite default database
- Docker
- Nginx config
- GitHub Actions CI/CD

## Ishga tushirish

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Migration

```bash
alembic upgrade head
```

Yangi migration yaratish:

```bash
alembic revision --autogenerate -m "change message"
alembic upgrade head
```

## Endpointlar

### Auth

- `POST /auth/register` — Ro‘yxatdan o‘tish
- `POST /auth/login` — Login qilish va JWT token olish

### Doctors

- `POST /doctors/` — Doctor qo‘shish
- `GET /doctors/` — Doctorlar ro‘yxati
- `GET /doctors/{doctor_id}` — Doctor detail ichida appointmentlar
- `PUT /doctors/{doctor_id}` — Doctorni tahrirlash
- `DELETE /doctors/{doctor_id}` — Doctorni o‘chirish

### Appointments

- `POST /appointments/` — Appointment booking
- `GET /appointments/` — Mening appointmentlarim
- `PATCH /appointments/{appointment_id}/status` — Appointment status update

## JWT Authentication

Login qilingandan keyin token olinadi. Swagger’da `Authorize` tugmasi bosiladi va token kiritiladi:

```text
Bearer YOUR_TOKEN
```

## Imtihonda tushuntirish

### Project structure

`app/main.py` — FastAPI app ishga tushadi va routerlar ulanadi.

`app/api/routes/` — endpointlar joylashgan.

`app/models/` — database table modellari.

`app/schemas/` — request va response validation.

`app/db/session.py` — database connection.

`app/core/security.py` — password hash va JWT token.

### Router

Router endpointlarni guruhlaydi. Masalan auth, doctors, appointments alohida routerlarda.

### Model

Model database table hisoblanadi. User, Doctor, Appointment modellari bor.

### Schema

Schema API orqali keladigan va qaytadigan ma’lumotlarni tekshiradi.

### CRUD

CRUD — Create, Read, Update, Delete. Doctorlar CRUD qilingan. Appointment booking va status update ham bor.

### JWT Authentication

JWT token user login qilgandan keyin beriladi. Himoyalangan endpointlarga token bilan kiriladi.

### Database connection

SQLAlchemy engine va SessionLocal orqali database ulanadi.

### Migration

Alembic database table o‘zgarishlarini boshqaradi.

### Deploy

Dockerfile orqali loyiha container qilinadi. Render, Railway, VPS yoki boshqa serverga deploy qilish mumkin.

### Nginx

Nginx reverse proxy vazifasini bajaradi. Tashqi requestlarni FastAPI serverga uzatadi.
