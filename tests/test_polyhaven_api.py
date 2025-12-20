from polyhaven.api import *

def test_is_api_available():
    assert is_api_available() is True

def test_get_types():
    assert get_types() == ["hdris", "textures", "models"]

def test_get_assets():
    assets = get_assets()
    assert isinstance(assets, dict)
    assert len(assets) > 0

def test_get_assets_by_type():
    for asset_type in ["hdris", "textures", "models"]:
        assets = get_assets_by_type(asset_type)
        assert isinstance(assets, dict)
        assert len(assets) > 0

def test_assets_have_thumbnail_url():
    """
    This test ensures that every asset retrieved from the PolyHaven API
    contains a valid 'thumbnail_url' field with a non-empty string value
    """

    assets = get_assets()
    assert len(assets) > 0, "Assets should be available"
    
    for asset_name, asset_data in assets.items():
        assert "thumbnail_url" in asset_data, f"Asset '{asset_name}' doesn't have 'thumbnail_url' field"
        assert isinstance(asset_data["thumbnail_url"], str), f"thumbnail_url for '{asset_name}' should be a string"
        assert asset_data["thumbnail_url"], f"thumbnail_url for '{asset_name}' should not be empty"
