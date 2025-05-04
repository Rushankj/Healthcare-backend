# Healthcare Backend API

![Profile Views](https://img.shields.io/github/watchers/Rushankj/Healthcare-backend?style=social)


A Django REST backend for healthcare management. Built this for a personal project to learn more about Django REST Framework.

## What's this?
This is a healthcare backend system I built with Django and DRF, using JWT auth (SimpleJWT package). Includes models for patients, doctors, and mappings between them.

## Project Structure
```
healthcare-backend/
├── env/                             # Your Python virtual environment
├── healthcaree/                     # Main Django project folder (created via startproject)
│   ├── manage.py                    # Django management script
│   ├── .env                         # (Optional) Environment variables file
│   ├── core/                        # Your Django app for healthcare logic
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   │       └── __init__.py
│   └── healthcare/                 # Django settings module (same name as the project)
│       ├── __init__.py
│       ├── settings.py             # Project settings (configured with PostgreSQL, JWT, etc.)
│       ├── urls.py
│       └── wsgi.py
├── requirements.txt                # (Optional) List of installed packages

```


## Features
- JWT Auth (login/logout) - nothing fancy but it works
- Patient CRUD operations 
- Doctor management
- Patient-Doctor mapping (because patients need doctors!)

## Setup (the usual Django stuff)

1. Clone it
```bash
git clone https://github.com/your-username/your-repo.git
cd healthcare-backed
```

2. Virtual env
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Get the requirements
```bash
pip install -r requirements.txt
```

4. Migrations
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

5. Make a superuser (you'll need this)
```bash
python manage.py createsuperuser
```

6. Fire it up!
```bash
python manage.py runserver
```

## API Endpoints

Here are the main endpoints - pretty standard REST stuff:

* **Login:** `POST /api/auth/login/`
* **Patients:** `GET|POST|PUT|DELETE /api/patients/`
* **Doctors:** `GET|POST|PUT|DELETE /api/doctors/`
* **Mappings:** `GET|POST|PUT|DELETE /api/mappings/`

You can use tools like Postman or curl to test these endpoints after getting your JWT token.

## Some JSON examples

### Login
```json
{
  "username": "admin",
  "password": "yourpassword"
}
```

![image](https://github.com/user-attachments/assets/f596c661-5efb-4a87-b5fd-4c3ab68cb910)


### Create a Patient
```json
{
  "user": 1,  // usually the logged-in user's ID
  "name": "John Doe",
  "age": 30,
  "gender": "Male",
  "address": "123 Main Street"
}
```

![image](https://github.com/user-attachments/assets/5d18dce5-d3d5-44a2-974c-b12c5c106755)



![image](https://github.com/user-attachments/assets/055da30c-923e-438d-a2ef-7f708223b20d)



Now, Hear i will add some forntend screenshots , the frontend will saw now is the one i used to test api for real usage . 
### Create a Doctor
```json
{
  "user": 1,
  "name": "Dr. Jane Smith",
  "specialty": "Cardiology",
  "phone": "123-456-7890"
}
```

![image](https://github.com/user-attachments/assets/ed120b82-7c68-4edb-9dc1-6c25408e5595)


### Map Patient to Doctor
```json
{
  "patient": 1,  // patient ID
  "doctor": 1,   // doctor ID
  "notes": "Follow-up in 2 weeks"
}
```

## Notes & Known Issues

- If you get CORS errors, check the CORS settings in settings.py
- Remember to include your JWT token in the Authorization header
- This is a assignment small  project, so expect some rough edges

## TODO (maybe someday)
- [ ] Add appointment scheduling
- [ ] Improve error handling
- [ ] Add better validation
- [ ] Write actual tests 😅

## License
Do whatever you want with this code. Credit appreciated but not required. No warranty expressed or implied!

---
If something's broken or you have questions, open an issue or reach out!
