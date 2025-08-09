import os, json
from playwright.sync_api import sync_playwright
from .helpers import BS, BS_USER, BS_KEY, BASE_URL, BS_DEVICE, BS_OS_VERSION

BS_WS = "wss://cdp.browserstack.com/playwright?caps="

def _bs_caps():
    return {
        "browser": "chromium",
        "device": BS_DEVICE,
        "osVersion": BS_OS_VERSION,
        "projectName": os.getenv("BS_PROJECT", "MobileSuite"),
        "buildName": os.getenv("BS_BUILD", "local-dev"),
        "sessionName": "Mobile Web Login",
        "client.playwrightVersion": os.getenv("PLAYWRIGHT_VERSION", "1.45.0"),
        "browserstack.username": BS_USER,
        "browserstack.accessKey": BS_KEY,
    }

class PageFactory:
    def __enter__(self):
        self.p = sync_playwright().start()
        if BS:
            ws = BS_WS + json.dumps(_bs_caps())
            self.browser = self.p.chromium.connect_over_cdp(ws)
            self.context = self.browser.contexts[0] if self.browser.contexts else self.browser.new_context()
        else:
            self.browser = self.p.chromium.launch()
            self.context = self.browser.new_context(viewport={"width": 412, "height": 915}, device_scale_factor=2)
        self.page = self.context.new_page()
        return self.page
    def __exit__(self, exc_type, exc, tb):
        self.context.close(); self.browser.close(); self.p.stop()
