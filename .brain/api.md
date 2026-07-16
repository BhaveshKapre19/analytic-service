# API Endpoints

## `POST /api/analytics/visit/`
Record a new visit.

**Request Body (JSON):**
```json
{
    "website_name": "Portfolio",
    "current_page": "/projects",
    "user_agent": "Mozilla/5.0...",
    "language": "en-US",
    "screen_resolution": "1920x1080",
    "timezone": "Asia/Kolkata",
    "session_id": "random_uuid",
    "referrer": "https://google.com",
    "country": "India",
    "region": "Madhya Pradesh",
    "city": "indore",
    "latitude": 21.3,
    "longitude": 76.2
}
```
*Note: Only `website_name` and `user_agent` are strictly required.*

**Response:**
```json
{
    "success": true
}
```

## Dashboard APIs

- `GET /api/dashboard/summary/`: Summary of total visits, daily visitor count, etc.
- `GET /api/dashboard/latest/`: Latest visitor records.
- `GET /api/dashboard/websites/`: Website-wise statistics.
