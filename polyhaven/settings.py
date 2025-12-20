from pathlib import Path
import json

# API and download settings
BASE_URL = "https://api.polyhaven.com"
HEADERS = {"User-Agent": "PolyHavenNukeBrowser"}
TIMEOUT = 10

# CDN settings
CDN_BASE_URLS = ("https://cdn.polyhaven.com", "https://cdn.polyhaven.org")
CDN_PREF_FILE = Path(__file__).resolve().parent / "cdn_preference.json"


def load_cdn_preference() -> str | None:
    """Load preferred CDN base URL from persistent storage."""
    try:
        with CDN_PREF_FILE.open("r", encoding="utf-8") as fp:
            preferred = json.load(fp).get("preferred_cdn")
        if preferred in CDN_BASE_URLS:
            return preferred
    except FileNotFoundError:
        return None
    except (json.JSONDecodeError, OSError):
        return None
    return None


def save_cdn_preference(base_url: str) -> None:
    """Save preferred CDN base URL to persistent storage."""
    if base_url not in CDN_BASE_URLS:
        return
    try:
        CDN_PREF_FILE.parent.mkdir(parents=True, exist_ok=True)
        with CDN_PREF_FILE.open("w", encoding="utf-8") as fp:
            json.dump({"preferred_cdn": base_url}, fp)
    except OSError:
        # If we cannot persist preference, continue without failing downloads.
        return
