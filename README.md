# Mobile Automation (RF + Appium + Playwright Python)

## Prereqs
- Python 3.10+
- BrowserStack account (Username/Access Key)

## Setup
1. python -m venv .venv && source .venv/bin/activate
2. pip install -r requirements.txt
3. python -m playwright install
4. cp .env.example .env (completa BASE_URL y BS_*)

## Run
- Mobile Web (local): pytest web/tests/test_web_login_smoke.py
- Mobile Web (BrowserStack): BROWSERSTACK=1 pytest web/tests/test_web_login_smoke.py
- Native Android (BrowserStack): robot -i smoke tests/mobile_native/smoke
## Test pipeline
Este cambio es solo para disparar el workflow mobile-ci.
