# Decisions

- **Database**: Started with SQLite for rapid development. Uses `django-environ` to easily swap to Postgres/Supabase later.
- **Parsing**: Using `user-agents` Python library rather than parsing on the frontend, because the frontend should be as light as possible.
- **IP Detection**: IP addresses are extracted in Django using `X-Forwarded-For` with a fallback to `REMOTE_ADDR` since frontends cannot reliably self-report their real IP.
