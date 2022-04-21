import pytest
import json
import unittest.mock as mock
from src.controllers.usercontroller import UserController

test_user = json.load(open("./test/unit/test_user.json"))
test_users = json.load(open("./test/unit/test_users.json"))
valid_email = "test@test.com"


# def test_get_user_by_email_valid_email_existing_user():
#     """ test get user by email with valid email and existing user """
#     # Arrange
#     mocked_dao = mock.MagicMock()
#     test_user = json.load(open("./test/unit/test_user.json"))
#     mocked_dao.find.return_value = test_user
#     sut = UserController(dao=mocked_dao)

#     # Act
#     valid_email = "test@test.com"
#     result = sut.get_user_by_email(valid_email)

#     # Assert
#     assert result["email"] == valid_email

def test_get_user_by_email_valid_email_multiple_existing_users_output(capsys):
    """ test output of get user by email with valid email and multiple existing users """
    # Arrange
    mocked_dao = mock.MagicMock()
    test_users = json.load(open("./test/unit/test_users.json"))
    mocked_dao.find.return_value = test_users
    sut = UserController(dao=mocked_dao)

    # Act
    valid_email = "test@test.com"
    sut.get_user_by_email(valid_email)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == f'Error: more than one user found with mail {valid_email}\n'

# Failing test
def test_get_user_by_email_valid_email_no_user():
    """ test get user by email with valid email and non existing user """
    # Arrange
    mocked_dao = mock.MagicMock()

    mocked_dao.find.return_value = []
    sut = UserController(dao=mocked_dao)

    # Act
    valid_email = "example@example.com"
    result = sut.get_user_by_email(valid_email)

    # Assert, raises IndexError and prints:
    # Error: more than one user found with mail example@example.com,
    # not returning None, as docstring says
    assert result == None

def test_get_user_by_email_invalid_email_try1():
    """ test get user by email with invalid email """
    # Arrange
    mocked_dao = mock.MagicMock()

    mocked_dao.find.return_value = []
    sut = UserController(dao=mocked_dao)

    # Act
    invalid_email = "test#test.com"
    error = "Error: invalid email address"

    with pytest.raises(ValueError) as e:
        sut.get_user_by_email(invalid_email)

    # Assert
    assert error == str(e.value)

def test_get_user_by_email_invalid_email_try2():
    """ test get user by email with invalid email """
    # Arrange
    mocked_dao = mock.MagicMock()

    mocked_dao.find.return_value = []
    sut = UserController(dao=mocked_dao)

    # Act
    invalid_email = "test@test"
    error = "Error: invalid email address"

    with pytest.raises(ValueError) as e:
        sut.get_user_by_email(invalid_email)

    # Assert
    assert error == str(e.value)

# Failing test
# def test_get_user_by_email_invalid_datatype():
#     """ test get user by email with invalid datatype for email """
#     # Arrange
#     mocked_dao = mock.MagicMock()

#     mocked_dao.find.return_value = []
#     sut = UserController(dao=mocked_dao)

#     # Act
#     invalid_datatype = 123

#     # Assert
#     # Throws TypeError: expected string or bytes-like object
#     with pytest.raises(ValueError) as e:
#         assert sut.get_user_by_email(invalid_datatype)


def test_get_user_by_email_raise_exception():
    """ test get user by email raise Exception """
    # Arrange
    mocked_dao = mock.MagicMock()

    mocked_dao.find.side_effect = Exception
    sut = UserController(dao=mocked_dao)

    # Act
    valid_email = "hej@hej.com"

    # Assert
    # Throws TypeError: expected string or bytes-like object
    with pytest.raises(Exception) as e:
        sut.get_user_by_email(valid_email)
