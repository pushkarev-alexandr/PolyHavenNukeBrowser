from urllib.request import urlopen, Request
import json

BASE_URL = "https://api.polyhaven.com"

def get_types() -> list[str]:
    req = Request(url = f"{BASE_URL}/types", headers = {"User-Agent": "PolyHavenNukeBrowser"})
    with urlopen(req, timeout=10) as resp:
        body: bytes = resp.read()
        data = json.loads(body.decode("utf-8"))

    return data
