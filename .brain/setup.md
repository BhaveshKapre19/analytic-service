# Setup Instructions

1. Clone or download the repository.
2. Open terminal in the `personalProject` folder.
3. Create a virtual environment (if not already present):
   `python -m venv venv`
4. Activate the virtual environment:
   `.\venv\Scripts\activate` (Windows)
   `source venv/bin/activate` (Mac/Linux)
5. Install requirements:
   `pip install -r requirements.txt`
6. Run migrations:
   `python manage.py migrate`
7. Start server:
   `python manage.py runserver`
