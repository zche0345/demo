from app import greet


def test_greet_returns_hello_world():
    assert greet() == "Hello world"
