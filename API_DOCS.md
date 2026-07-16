# 📊 Analytics Backend API Documentation

Welcome to the API Documentation for the Analytics Backend! This document outlines how to interact with the endpoints available in the system.

## Base URL
When running locally, the base URL is:
`http://127.0.0.1:8000/`

---

## 🚀 1. Track Visit
Records a new visitor session for a given website.

*   **URL**: `/api/analytics/visit/`
*   **Method**: `POST`
*   **Content-Type**: `application/json`

### Request Body
| Field | Type | Required | Description |
|---|---|---|---|
| `website_name` | String | **Yes** | Identifier for the frontend website (e.g., "Portfolio", "Chess App") |
| `user_agent` | String | **Yes** | The raw `navigator.userAgent` string from the browser. |
| `language` | String | No | Browser language (e.g., "en-US") |
| `screen_resolution` | String | No | e.g., "1920x1080" |
| `timezone` | String | No | e.g., "Asia/Kolkata" |
| `session_id` | String | No | A unique identifier for the user's session |
| `referrer` | String | No | The URL the user came from (`document.referrer`) |
| `current_page` | String | No | The current route or page URL |
| `country` | String | No | Optional GeoIP data |
| `city` | String | No | Optional GeoIP data |
| `latitude` | Float | No | Optional GeoIP data |
| `longitude` | Float | No | Optional GeoIP data |

*Note: The client's IP address is automatically extracted by the backend using `X-Forwarded-For` and `REMOTE_ADDR` headers.*

### Example Request
```json
{
    "website_name": "Personal Portfolio",
    "current_page": "/about-me",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "language": "en-US",
    "screen_resolution": "1920x1080",
    "timezone": "Asia/Kolkata",
    "session_id": "ab12-cd34-ef56",
    "referrer": "https://google.com",
    "country": "India",
    "city": "Mumbai"
}
```

### Response
```json
{
    "success": true
}
```
*(Status Code: 201 Created)*

---

## 📈 2. Dashboard APIs
The following GET endpoints are designed for building an analytics dashboard.

### 2.1 Get Summary Statistics
*   **URL**: `/api/dashboard/summary/`
*   **Method**: `GET`
*   **Response**: Returns totals across the entire platform.
```json
{
  "total_visits": 1500,
  "visits_today": 45,
  "unique_visitors": 1200
}
```

### 2.2 Get Latest Visits
*   **URL**: `/api/dashboard/latest/`
*   **Method**: `GET`
*   **Response**: Returns an array of the 10 most recent visitor records.
```json
[
  {
    "id": 45,
    "website": "Personal Portfolio",
    "ip": "192.168.1.102",
    "country": "India",
    "browser": "Chrome",
    "device": "PC",
    "timestamp": "2026-07-16T10:45:00.000Z"
  }
]
```

### 2.3 Get Website Breakdowns
*   **URL**: `/api/dashboard/websites/`
*   **Method**: `GET`
*   **Response**: Returns visit statistics aggregated by each unique website name, sorted by highest traffic.
```json
[
  {
    "website_name": "Personal Portfolio",
    "total_visits": 1200,
    "unique_ips": 950
  },
  {
    "website_name": "Chess Website",
    "total_visits": 300,
    "unique_ips": 250
  }
]
```
