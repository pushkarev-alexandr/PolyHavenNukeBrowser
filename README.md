# Poly Haven Nuke Browser

An asset manager for https://polyhaven.com/
An analogue of the Blender add-on https://github.com/Poly-Haven/polyhavenassets, but for Nuke

Uses the API:
- Landing page about the API: https://polyhaven.com/our-api
- API documentation: https://redocly.github.io/redoc/?url=https://api.polyhaven.com/api-docs/swagger.json&nocors
- API repository: https://github.com/Poly-Haven/Public-API

Important:
- All API requests must include a unique User-Agent header (e.g. your app name) so Poly Haven can track usage.

Requirements:
- Load information about assets
- Create asset cards with an image and caption using QListWidget and QListWidgetItem
- Images load in parallel so the UI is interactive while images may still be loading
- Images load using multithreading for speed
- Cards can be dragged to drop into the Nuke interface
- When a card is dropped, it is processed separately
- Set the download size and format, and only then perform the download

Available endpoints:
- https://api.polyhaven.com/assets — all assets
- https://api.polyhaven.com/assets?t=[type] — filter by type, e.g. https://api.polyhaven.com/assets?t=hdris
- https://api.polyhaven.com/types — view available types; currently returns ["hdris","textures","models"]
- https://api.polyhaven.com/categories/[type] — view categories for a type, e.g. https://api.polyhaven.com/categories/textures
- https://api.polyhaven.com/assets?t=[type]&c=[category] — filter by type and category, e.g. https://api.polyhaven.com/assets?t=models&c=furniture
- https://api.polyhaven.com/assets?c=[category] — filter by category only
- https://api.polyhaven.com/info/[asset_id] — view information about an asset, e.g. https://api.polyhaven.com/info/ArmChair_01
- https://api.polyhaven.com/files/[asset_id] — view files for an asset, e.g. https://api.polyhaven.com/files/aerial_asphalt_01
- https://api.polyhaven.com/api-docs/swagger.json - here you can view the full configuration and API capabilities


Configuration requirements:
- Ability to set the folder where downloaded asset previews are stored
- Ability to set the folder where asset files are stored
- A default path should be set within the plugin’s current folder

API usage
- User-Agent requirement: The Poly Haven API requires a unique User-Agent header for all requests.
- Default behavior: The library sends a default UA like "PolyHavenNukeBrowser/0.1 (Python/X.Y.Z; OS Version)".
- Configure via env var: Set POLYHAVEN_USER_AGENT to override globally.
- Configure in code:

```python
from polyhaven.api import set_user_agent, get_types

set_user_agent("MyPolyHavenApp/1.0 (+https://example.com)")
types = get_types()  # ["hdris", "textures", "models"]

# or per-call override
types = get_types(user_agent="MyPolyHavenApp/1.0")
```
