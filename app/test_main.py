import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected_result", [
    ("", True),
    ("hello", False),
    ("world", True),
    ("Python", True),
    ("racecar", False),
    ("abracadabra", False),
    ("12345", True),
    ("aA", False),
])
def test_is_isogram(
        word: str,
        expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
