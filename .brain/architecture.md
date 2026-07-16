# Analytics Backend Architecture

## Overview
This is a Django REST Framework backend designed to collect and serve visitor analytics from multiple frontend React applications.

## Key Components
- **Django Project (`config`)**: Holds global settings, URL routing, and WSGI/ASGI configurations.
- **Tracker App (`tracker`)**: The core application that handles data ingestion, modeling, and API endpoints.
- **Database**: SQLite (local dev), easily migratable to PostgreSQL/Supabase via `django-environ`.

## Data Flow
1. React Frontend sends a POST request to `/api/analytics/visit/`.
2. The `VisitRecord` view extracts the client IP and parses the User-Agent string.
3. The data is validated using `VisitorSerializer`.
4. A `Visitor` model instance is created and saved to the database.
5. The Django Admin panel and Dashboard API endpoints can be used to view the aggregated statistics.
