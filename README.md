(run instructions)
# E-Notice Board (Django)

## Setup (VS Code)

1. Open VS Code and open this project folder.
2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # mac/linux
   source venv/bin/activate
3.	Install dependencies:
 	pip install -r requirements.txt
4.	Create .env from .env.example and set SECRET_KEY and DEBUG as needed.
5.	Run migrations:
 	python manage.py migrate
6.	Create superuser (admin):
 	python manage.py createsuperuser
7.	Collect static (optional for production):
 	python manage.py collectstatic
8.	Run development server:
 	python manage.py runserver
9.	Open http://127.0.0.1:8000/ in your browser.
o	Admin: http://127.0.0.1:8000/admin/
10.	To allow file uploads during development, MEDIA_ROOT and MEDIA_URL are already configured; uploaded files will be in the media/ folder.
Notes
•	Timezone is set to Asia/Kolkata.
•	For production use, set DEBUG=False and configure allowed hosts, static files, and media properly.

---

## Extra: Helpful commands (copy-paste)

```bash
# create and enter venv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
