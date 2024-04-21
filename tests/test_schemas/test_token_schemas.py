import pytest
from app.schemas.token_schemas import Token, TokenData, RefreshTokenRequest

@pytest.fixture
def example_access_token():
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

@pytest.fixture
def example_username():
    return "user@example.com"

@pytest.fixture
def example_refresh_token():
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

def test_token_model_with_example_access_token(example_access_token):
    token = Token(access_token=example_access_token)
    assert token.access_token == example_access_token
    assert token.token_type == "bearer"

def test_token_data_model_with_example_username(example_username):
    token_data = TokenData(username=example_username)
    assert token_data.username == example_username

def test_refresh_token_request_model_with_example_refresh_token(example_refresh_token):
    refresh_request = RefreshTokenRequest(refresh_token=example_refresh_token)
    assert refresh_request.refresh_token == example_refresh_token