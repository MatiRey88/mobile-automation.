import os
from dotenv import load_dotenv
load_dotenv()

BS = os.getenv("BROWSERSTACK", "0") == "1"
BS_USER = os.getenv("BS_USERNAME")
BS_KEY = os.getenv("BS_ACCESS_KEY")
BASE_URL = os.getenv("BASE_URL") or "https://www.networksolutions.com"
BS_DEVICE = os.getenv("BS_DEVICE", "Google Pixel 7")
BS_OS_VERSION = os.getenv("BS_OS_VERSION", "13.0")
