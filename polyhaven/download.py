from urllib.request import urlopen, Request
import os

from .settings import CDN_BASE_URLS, HEADERS, TIMEOUT, load_cdn_preference, save_cdn_preference


def download_file(src_url: str, dest_path: str, timeout: int = TIMEOUT) -> str:
    """Download a file from URL to destination path."""
    # Ensure destination directory exists
    final_dir = os.path.dirname(dest_path)
    if final_dir:
        os.makedirs(final_dir, exist_ok=True)

    req = Request(url=src_url, headers=HEADERS)
    try:
        with urlopen(req, timeout=timeout) as resp:
            data = resp.read()
    except Exception as exc:
        raise RuntimeError(f"Failed to download {src_url}: {exc}") from exc

    with open(dest_path, "wb") as out_file:
        out_file.write(data)

    return dest_path


def download_thumbnail(asset_name: str, timeout: int = TIMEOUT) -> str:
    """Download thumbnail for an asset, with CDN fallback and preference tracking."""
    url_path = f"/asset_img/thumbs/{asset_name}.png?width=256&height=256"
    thumbnail_dest = f"temp/{asset_name}.png"
    preferred = load_cdn_preference()
    bases = [preferred] if preferred else []
    bases += [base for base in CDN_BASE_URLS if base not in bases]

    last_error = None
    for base_url in bases:
        try:
            download_file(base_url + url_path, thumbnail_dest, timeout=timeout)
        except Exception as exc:
            last_error = exc
            continue
        save_cdn_preference(base_url)
        return thumbnail_dest

    if last_error:
        raise last_error
    raise RuntimeError("Failed to download thumbnail from available CDNs")
