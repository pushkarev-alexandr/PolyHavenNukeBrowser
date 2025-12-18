from polyhaven.api import get_types

def test_get_types():
    assert get_types() == ["hdris", "textures", "models"]
