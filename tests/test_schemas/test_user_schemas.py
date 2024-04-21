import uuid
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest

# Fixtures for common test data
@pytest.fixture
def user_base_data():
    return {
        "username": "john_doe_123",
        "email": "john.doe@example.com",
        "full_name": "John Doe",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg"
    }

@pytest.fixture
def user_create_data(user_base_data):
    return {**user_base_data, "password": "SecurePassword123!"}

@pytest.fixture
def user_update_data():
    return {
        "email": "john.doe.new@example.com",
        "full_name": "John H. Doe",
        "bio": "I specialize in backend development with Python and Node.js.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe_updated.jpg"
    }

@pytest.fixture
def user_response_data():
    return {
        "id": "unique-id-string",
        "username": "testuser",
        "email": "test@example.com",
        "last_login_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "links": []
    }

@pytest.fixture
def login_request_data():
    return {"username": "john_doe_123", "password": "SecurePassword123!"}

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.username == user_base_data["username"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.username == user_create_data["username"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_partial(user_update_data):
    partial_data = {"email": user_update_data["email"]}
    user_update = UserUpdate(**partial_data)
    assert user_update.email == partial_data["email"]

# Tests for UserResponse
def test_user_response_datetime(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.last_login_at == user_response_data["last_login_at"]
    assert user.created_at == user_response_data["created_at"]
    assert user.updated_at == user_response_data["updated_at"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.username == login_request_data["username"]
    assert login.password == login_request_data["password"]

# Parametrized tests for username and email validation
@pytest.mark.parametrize("username", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_username_valid(username, user_base_data):
    user_base_data["username"] = username
    user = UserBase(**user_base_data)
    assert user.username == username

@pytest.mark.parametrize("username", ["test user", "test?user", "", "us", "JohnDoe1234567890", "test_user."])
def test_user_base_username_invalid(username, user_base_data):
    user_base_data["username"] = username
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

@pytest.mark.parametrize("password", ["SecurePassword123@", "SecurePassword123@SecurePassword123@SecurePassword123@"])
def test_valid_password_for_user_creation(password, user_create_data):
    user_create_data["password"] = password
    user = UserCreate(**user_create_data)
    assert user.password == password
    
@pytest.mark.parametrize("password", ["Secure Password", "", "SecurePassword123", "securepassword123@", "securepassword1234", "securepassword1234!", "kdslhlskdhflskdlskdhflshdlksdflsdhflshdglshdlghsdlvs;ldvh;lsvh;lskchv;lsdfhv;kfvlkdfhvld"])
def test_invalid_password_for_user_creation(password, user_base_data):
    user_base_data["password"] = password
    with pytest.raises(ValidationError):
        UserCreate(**user_base_data)

def test_user_update_partial_with_full_name(user_update_data):
    partial_data = {"email": user_update_data["email"], "full_name": user_update_data["full_name"]}
    user_update = UserUpdate(**partial_data)
    assert user_update.email == partial_data["email"]
    assert user_update.full_name == partial_data["full_name"]
    
def test_user_update_with_invalid_link(user_update_data):
    partial_data = {"email": user_update_data["email"], "profile_picture_url": "https://google.com/"}
    with pytest.raises(ValidationError):
        UserUpdate(**partial_data)

@pytest.mark.parametrize("full_name", ["Hello world 1234"])
def test_user_base_full_name_invalid(full_name, user_base_data):
    user_base_data["full_name"] = full_name
    with pytest.raises(ValidationError):
        UserCreate(**user_base_data)
