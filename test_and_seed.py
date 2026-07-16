import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client

def run_tests():
    client = Client()
    
    # 1. Test POST /api/analytics/visit/
    payloads = [
        {
            "website_name": "Portfolio",
            "current_page": "/projects",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "language": "en-US",
            "screen_resolution": "1920x1080",
            "timezone": "Asia/Kolkata",
            "session_id": "session_123",
            "referrer": "https://google.com",
            "country": "India",
            "city": "Mumbai"
        },
        {
            "website_name": "Chess Website",
            "current_page": "/play",
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
            "language": "en-GB",
            "screen_resolution": "390x844",
            "timezone": "Europe/London",
            "session_id": "session_456",
            "country": "UK",
            "city": "London"
        },
        {
            "website_name": "Portfolio",
            "current_page": "/",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "language": "en-US",
            "screen_resolution": "2560x1440",
            "timezone": "America/New_York",
            "session_id": "session_789",
            "country": "USA",
            "city": "New York"
        }
    ]
    
    print("========================================")
    print("Testing POST /api/analytics/visit/...")
    print("========================================")
    for i, data in enumerate(payloads):
        # We simulate REMOTE_ADDR for IP
        ip = f'192.168.1.10{i}'
        response = client.post('/api/analytics/visit/', data=json.dumps(data), content_type='application/json', REMOTE_ADDR=ip)
        print(f"[{data['website_name']}] Status: {response.status_code} | Response: {response.json()}")
        
    print("\n========================================")
    print("Testing GET /api/dashboard/summary/...")
    print("========================================")
    response = client.get('/api/dashboard/summary/')
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    
    print("\n========================================")
    print("Testing GET /api/dashboard/websites/...")
    print("========================================")
    response = client.get('/api/dashboard/websites/')
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

    print("\n========================================")
    print("Testing GET /api/dashboard/latest/...")
    print("========================================")
    response = client.get('/api/dashboard/latest/')
    print(f"Status: {response.status_code}")
    print(f"Returned {len(response.json())} records. First record sample:")
    if response.json():
        print(json.dumps(response.json()[0], indent=2))

if __name__ == '__main__':
    run_tests()
