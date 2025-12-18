from polyhaven.api import get_types, is_api_available

def test_get_types():
    assert get_types() == ["hdris", "textures", "models"]


def test_is_api_available():
    assert is_api_available() is True
