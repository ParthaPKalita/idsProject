
TEST_CASE = [
    # ----------------------------------
    # 1. Normal traffic test cases
    # ----------------------------------
    {
        "test_id": "normal_001",
        "category": "normal",
        "method": "GET",
        "path": "/",
        "payload": None,
    },
    {
        "test_id": "normal_002",
        "category": "normal",
        "method": "GET",
        "path": "/robots.txt",
        "payload": None,
    },
    {
        "test_id": "normal_003",
        "category": "normal",
        "method": "GET",
        "path": "/rest/products/search?q=apple",
        "payload": None,
    },
    {
        "test_id": "normal_004",
        "category": "normal",
        "method": "GET",
        "path": "/rest/products/search?q=banana",
        "payload": None,
    },
    {
        "test_id": "normal_005",
        "category": "normal",
        "method": "GET",
        "path": "/api/Challenges",
        "payload": None,
    },

    # ----------------------------------
    # 2. Normal login test cases
    # ----------------------------------
    {
        "test_id": "login_001",
        "category": "normal_login",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "test1@example.com",
            "password": "invalid-test-password",
        },
    },
    {
        "test_id": "login_002",
        "category": "normal_login",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "test2@example.com",
            "password": "another-invalid-password",
        },
    },
    {
        "test_id": "login_003",
        "category": "normal_login",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "student@example.com",
            "password": "wrong-password",
        },
    },

    # ----------------------------------
    # 3. SQL injection detection tests
    # ----------------------------------
    {
        "test_id": "sqli_001",
        "category": "sqli_test",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "' OR 1=1 --",
            "password": "test",
        },
    },
    {
        "test_id": "sqli_002",
        "category": "sqli_test",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "' OR '1'='1' --",
            "password": "test",
        },
    },
    {
        "test_id": "sqli_003",
        "category": "sqli_test",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "admin'--",
            "password": "test",
        },
    },
    {
        "test_id": "sqli_004",
        "category": "sqli_test",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "' OR 1=1#",
            "password": "test",
        },
    },
    {
        "test_id": "sqli_005",
        "category": "sqli_test",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "' OR 'a'='a",
            "password": "test",
        },
    },
    {
        "test_id": "sqli_006",
        "category": "sqli_test",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "test' AND '1'='2",
            "password": "test",
        },
    },
    {
        "test_id": "sqli_007",
        "category": "sqli_test",
        "method": "POST",
        "path": "/rest/user/login",
        "payload": {
            "email": "normal-test-value' OR 1=1 --",
            "password": "test",
        },
    },
]
