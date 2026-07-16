# Analytics Backend

A production-ready Django REST Framework backend designed to receive and store visitor analytics from multiple React frontend websites.

## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- `pip`

### 2. Installation
Clone this repository and open a terminal in the project root directory.

If you don't have a virtual environment yet, create one:
```bash
python -m venv venv
```

Activate the virtual environment:
- Windows: `.\venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

Install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
The project uses `.env` for environment variables. Ensure the `.env` file exists in the root directory.
```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 4. Database Migration
Run the initial migrations to create the database schema:
```bash
python manage.py makemigrations tracker
python manage.py migrate
```

### 5. Create Superuser
Create an admin account to access the Django Admin panel:
```bash
python manage.py createsuperuser
```

### 6. Run Server
Start the development server:
```bash
python manage.py runserver
```
You can access the Django Admin at `http://127.0.0.1:8000/admin/`.

## API Documentation

See `.brain/api.md` for full details.

### Track Visit
`POST /api/analytics/visit/`
Sends visitor data. The `website_name` and `user_agent` are required. IP address is automatically extracted on the backend.

### Dashboard Stats
- `GET /api/dashboard/summary/`: Summary stats (Total, Today, Unique).
- `GET /api/dashboard/latest/`: The last 10 visits.
- `GET /api/dashboard/websites/`: Visit statistics grouped by website name.

## Future Deployment
The project is configured to use `django-environ`. For production (e.g. Supabase, AWS RDS, DigitalOcean), simply update the `DATABASE_URL` in your production environment variables to your Postgres connection string (e.g. `postgres://user:pass@host:port/dbname`) and install `psycopg2-binary`. The application will automatically switch to using it without code changes.
