import os, requests
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
def seed_user(email: str, password: str):
    r = requests.post(f"{BASE_URL}/api/test/seed_user", json={"email": email, "password": password}, timeout=10)
    r.raise_for_status()
    return r.json()
