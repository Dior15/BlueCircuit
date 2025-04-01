import pytest
from unittest.mock import MagicMock, patch
from login import UserLogin
from models import User
from app import app

def testSignupMissingFields():
    # Test signup with missing fields
    response, status = UserLogin.signup("", "test", "pass", "pass")
    assert not response["success"]
    assert status == 400

def testSignupPasswordMismatch():
    # Test signup with non-matching passwords
    response, status = UserLogin.signup("test@example.com", "test", "pass1", "pass2")
    assert not response["success"]
    assert status == 400

def testLoginMissingFields():
    # Test login with missing input
    response, status = UserLogin.login("", "")
    assert not response["success"]
    assert status == 400

@patch("login.session", {})
def testCheckLoginNotLoggedIn():
    # Test check_login without session
    response, status = UserLogin.check_login()
    assert not response["logged_in"]
    assert status == 200
