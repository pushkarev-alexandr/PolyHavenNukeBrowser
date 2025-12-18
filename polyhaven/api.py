from urllib.request import urlopen, Request
import json

BASE_URL = "https://api.polyhaven.com"
HEADERS = {"User-Agent": "PolyHavenNukeBrowser"}
TIMEOUT = 10

def get_types() -> list[str]:
    req = Request(url=f"{BASE_URL}/types", headers=HEADERS)
    with urlopen(req, timeout=TIMEOUT) as resp:
        body = resp.read()
        data = json.loads(body.decode("utf-8"))

    return data

def is_api_available() -> bool:
    req = Request(url=BASE_URL, headers=HEADERS)
    with urlopen(req, timeout=TIMEOUT) as resp:
        return resp.getcode() == 200
