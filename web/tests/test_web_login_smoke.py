import os, re
from .bs_driver import PageFactory

BASE_URL = os.getenv("BASE_URL", "https://www.networksolutions.com")

def test_homepage_loads_and_header_present():
    with PageFactory() as page:
        page.goto(BASE_URL)
        title = page.title()
        assert re.search(r"Network\s+Solutions", title, re.IGNORECASE)
        page.get_by_role("navigation").wait_for(timeout=15000)
