import json, os
from typing import Optional
import requests

BS_SESS_API = "https://api.browserstack.com/automate/sessions/{session_id}.json"

def mark(status: str, reason: str, session_id: Optional[str] = None):
    assert status in {"passed", "failed"}
    user = os.getenv("BS_USERNAME"); key = os.getenv("BS_ACCESS_KEY")
    if not user or not key:
        print("[bs_session] Missing BS credentials"); return
    if not session_id:
        session_id = os.getenv("BROWSERSTACK_SESSION_ID")
    if not session_id:
        print("[bs_session] Missing session_id"); return
    url = BS_SESS_API.format(session_id=session_id)
    payload = {"status": status, "reason": reason}
    r = requests.put(url, auth=(user, key), json=payload, timeout=15)
    print("[bs_session]", r.status_code, r.text)
