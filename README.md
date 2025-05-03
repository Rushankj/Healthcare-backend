Here's your complete `README.md` file in one tab-friendly format:

```markdown
# Healthcare Backend API with Django + Frontend Test Interface

This project is a healthcare backend system built using **Django** and **Django REST Framework**, with **JWT authentication** via SimpleJWT. It includes models for patients, doctors, and their mappings, and provides API endpoints for full CRUD operations. A simple HTML+JavaScript frontend is included to test the API without needing tools like Postman.

## 📁 Project Structure

```

healthcare-backed/
├── backend/             # Django project and apps
│   ├── manage.py
│   ├── healthcare/      # Django settings
│   ├── api/             # DRF views, serializers, models
├── frontend/
│   └── index.html       # Frontend to interact with API
├── .gitignore
└── README.md

````

## 🚀 Features

- JWT Authentication (Login/Logout)
- Patient Management (Create, Read, Update, Delete)
- Doctor Management
- Patient-Doctor Mapping
- API tested via in-browser frontend (`index.html`)

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd healthcare-backed
````

### 2. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

## 🌐 API Access

* **Login:** `POST /api/auth/login/`
* **Patients:** `GET|POST|PUT|DELETE /api/patients/`
* **Doctors:** `GET|POST|PUT|DELETE /api/doctors/`
* **Mappings:** `GET|POST|PUT|DELETE /api/mappings/`

Use the browser-based frontend (`frontend/index.html`) to test these routes easily after login.

## 📄 JSON Body Examples

### 🔐 Login

```json
{
  "username": "admin",
  "password": "yourpassword"
}
```

### ➕ Create Patient

```json
{
  "user": 1,
  "name": "John Doe",
  "age": 30,
  "gender": "Male",
  "address": "123 Main Street"
}
```

### ➕ Create Doctor

```json
{
  "user": 1,
  "name": "Dr. Jane Smith",
  "specialty": "Cardiology",
  "phone": "123-456-7890"
}
```

### 🔗 Map Patient to Doctor

```json
{
  "patient": 1,
  "doctor": 1,
  "notes": "Follow-up in 2 weeks"
}
```

## 💡 Notes

* Ensure the backend is running before using the frontend (`index.html`).
* You can test all API operations from the browser without Postman.
* Adjust `user` fields to match the logged-in user ID (typically 1 for superuser).

## 📜 License

This project is for educational/demo purposes and doesn't include a formal license. You're welcome to adapt it for your needs.

```

Would you also like me to generate a `.gitignore` file suited for a Django project?
```
