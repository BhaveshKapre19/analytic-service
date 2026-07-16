# Database Documentation

The project uses SQLite by default for easy local development.

The connection string is read from the `.env` file using the `django-environ` package.

`DATABASE_URL=sqlite:///db.sqlite3`

## Deploying to Production
To use PostgreSQL or Supabase in production:
1. Update the `.env` file with your PostgreSQL connection URL:
   `DATABASE_URL=postgres://user:password@host:port/database`
2. Install the psycopg2 package:
   `pip install psycopg2-binary`
3. Restart the server.

The settings.py file is already configured to automatically read this environment variable and switch the database.
