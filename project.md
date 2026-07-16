You are a Senior Python Backend Engineer and Django REST Framework Architect.

Your task is to build a production-quality Django REST Framework backend that will receive visitor analytics from multiple React websites.

The project should be clean, modular, documented, scalable, and follow Django best practices.

====================================================
PROJECT GOAL
====================================================

Create a Django REST API backend that records visitor information sent from multiple React applications.

Initially I have two React websites.

1. Personal Portfolio
2. Chess Website

Both React applications will send analytics to this backend.

The backend should be generic so more websites can be added later without modifying the database schema.

====================================================
ENVIRONMENT SETUP
====================================================

The AI MUST perform proper project setup.

Create and use a Python virtual environment.

Example

python -m venv venv

Activate it.

Install all required packages.

Generate a requirements.txt.

Use latest stable versions whenever possible.

Packages should include at least:

Django
djangorestframework
django-cors-headers
django-filter
python-dotenv
user-agents
django-environ

If GeoIP is implemented, install required package.

====================================================
PROJECT STRUCTURE
====================================================

Create a clean project structure.

analytics_backend/

    config/

    analytics/

    venv/

    .brain/

    requirements.txt

    .env

    .gitignore

    README.md

====================================================
BRAIN FOLDER
====================================================

Create a ".brain" folder.

This folder stores documentation for future AI assistants.

Generate files such as:

.brain/

    architecture.md

    api.md

    models.md

    database.md

    coding_rules.md

    setup.md

    dependencies.md

    roadmap.md

    decisions.md

    changelog.md

    endpoints.md

    testing.md

    future_features.md

Each document should explain the project thoroughly.

Future AI assistants should understand the entire project simply by reading this folder.

====================================================
DATABASE MODEL
====================================================

Create a Visitor model.

Fields:

id

website_name

visitor_ip

country (optional)

region (optional)

city (optional)

latitude (optional)

longitude (optional)

browser

browser_version

operating_system

device_type

device_brand

device_model

is_mobile

is_tablet

is_pc

user_agent

language

screen_resolution (optional)

timezone (optional)

referrer (optional)

current_page

session_id

visit_timestamp

created_at

updated_at

====================================================
LOCATION
====================================================

Location is OPTIONAL.

The React frontend may send:

country

city

region

latitude

longitude

If frontend does not send location, save null.

Never fail because of missing location.

====================================================
IP ADDRESS
====================================================

Do NOT trust the IP sent from frontend.

Always detect the real client IP from the Django request.

Support:

X-Forwarded-For

REMOTE_ADDR

Store detected IP.

====================================================
USER AGENT
====================================================

Frontend will send complete navigator.userAgent string.

Backend should parse it using user-agents package.

Extract:

browser

browser version

operating system

device type

mobile

tablet

desktop

device brand

device model

====================================================
API
====================================================

Create REST endpoints.

POST

/api/analytics/visit/

Receives JSON

Example

{
    "website_name":"Portfolio",
    "current_page":"/projects",
    "user_agent":"...",
    "language":"en-US",
    "screen_resolution":"1920x1080",
    "timezone":"Asia/Kolkata",
    "session_id":"random_uuid",
    "referrer":"https://google.com",
    "country":"India",
    "region":"Madhya Pradesh",
    "city":"Burhanpur",
    "latitude":21.3,
    "longitude":76.2
}

Response

{
    "success":true
}

====================================================
VALIDATION
====================================================

website_name required

user_agent required

Everything else optional.

====================================================
CORS
====================================================

Configure django-cors-headers.

Allow localhost during development.

Allow easy addition of production React domains later.

====================================================
ADMIN PANEL
====================================================

Customize Django Admin.

Visitor list should display

Website

IP

Browser

Device

Country

Visit Time

Search:

IP

Website

Browser

Country

Filter:

Website

Country

Device

Date

====================================================
API DOCUMENTATION
====================================================

Document every endpoint inside README.md.

====================================================
README
====================================================

Generate complete README including

Installation

Virtual Environment

Running server

Migration

API endpoints

Folder structure

Future deployment

====================================================
CODE QUALITY
====================================================

Use

Class Based Views

DRF serializers

Separate services where appropriate

Settings split if needed

Environment variables

Comments where useful

PEP8 formatting

====================================================
BONUS FEATURES
====================================================

If possible also implement:

Daily visitor count

Unique visitors by IP

Website-wise statistics

Total visits

Latest visits endpoint

Dashboard statistics endpoint

Example

/api/dashboard/

/api/dashboard/summary/

/api/dashboard/latest/

/api/dashboard/websites/

====================================================
SECURITY
====================================================

Rate limit if possible.

Validate all inputs.

Protect against malformed requests.

Never trust frontend IP.

====================================================
REACT INTEGRATION
====================================================

At the end create

analytics.js

Example React function

sendVisitorAnalytics()

that automatically collects

website name

navigator.userAgent

language

screen resolution

timezone

referrer

current page

session id

(optional location)

and sends POST request to Django backend.

====================================================
FINAL OUTPUT
====================================================

The final project should run immediately after

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

with no manual fixes required.

Produce production-quality code.