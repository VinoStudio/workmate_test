example_logs = [
    {
        "url": "/api/test",
        "response_time": 150,
        "@timestamp": "2025-06-22T10:00:00",
        "http_user_agent": "...",
        "status": 200,
    },
    {
        "url": "/api/users",
        "response_time": 100,
        "@timestamp": "2025-06-22T10:01:00",
        "http_user_agent": "...",
        "status": 200,
    },
    {
        "url": "/api/products",
        "response_time": 50,
        "@timestamp": "2025-06-22T10:02:00",
        "user_agent": "...",
        "status": 404,
    },
    {
        "url": "/api/orders",
        "response_time": 300,
        "@timestamp": "2025-06-22T10:03:00",
        "http_user_agent": "...",
        "status": 201,
    },
    {
        "url": "/api/profile",
        "response_time": 200,
        "@timestamp": "2025-06-22T10:04:00",
        "http_user_agent": "...",
        "status": 200,
    },
]

invalid_log = [
    {"@timestamp": "2025-06-22T10:00:00", "url": "/api/test", "response_time": 100},
    {"invalid": "json"},
    {"timestamp": "2025-06-22T10:00:00"},
]
