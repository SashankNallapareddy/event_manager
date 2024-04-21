import pytest
from datetime import datetime, timedelta
from app.utils.common import authenticate_user, create_access_token, validate_and_sanitize_url, verify_refresh_token
from app.dependencies import get_settings
from fastapi import HTTPException, status

settings = get_settings()

def test_authenticate_user_valid():
    result = authenticate_user("admin", "secret")
    assert result == {"username": "admin"}
    
def test_authenticate_user_invalid():
    result = authenticate_user("admin", "wrongpassword")
    assert result is None

def test_create_access_token_for_10_mins():
    token = create_access_token({"sub": "user"}, timedelta(minutes=10))
    assert isinstance(token, str) and token != ""
    
def test_create_access_token_for_2_hour():
    token = create_access_token({"sub": "user"}, timedelta(hours=2))
    assert isinstance(token, str) and token != ""

def test_validate_and_sanitize_url_for_valid_url():
    # Act
    result = validate_and_sanitize_url("http://google.com")
    # Assert
    assert result == "http://google.com"
    
def test_validate_and_sanitize_url_for_invalid_url():
    # Act
    result = validate_and_sanitize_url("google")
    # Assert
    assert result is None

def test_verify_refresh_token_for_valid_token():
    result = verify_refresh_token(create_access_token({"sub": "user"}, timedelta(minutes=10)))
    assert result == {"username": "user"}

def test_verify_refresh_token_for_invalid_token():
    with pytest.raises(HTTPException) as exc_info:
        verify_refresh_token(create_access_token({"sub2": "user"}, timedelta(minutes=10)))
    assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
    
def test_verify_refresh_token_for_invalid_token2():
    with pytest.raises(HTTPException) as exc_info:
        verify_refresh_token("invalid_token")
    assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED