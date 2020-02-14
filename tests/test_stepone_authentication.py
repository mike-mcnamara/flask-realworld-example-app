# coding: utf-8

from flask import url_for
from conduit.exceptions import USER_ALREADY_REGISTERED


def _register_user(testapp, **kwargs):
    return testapp.post_json(url_for("user.register_user"), {
        "user": {
            "username": "mo",
            "email": "mo@mo.mo",
            "password": "momo"
        }
    }, **kwargs)


class TestAuthenticate:

    def test_register_user(self, testapp):
        # register user and get response

        # assert properties like email and valid token
        None

    def test_user_login(self, testapp):
        # register user

        # post login request

        # assert response properties
        None

    def test_get_user(self, testapp):
        # register user and get token

        # get user object using token and assert properties
        None

    def test_register_already_registered_user(self, testapp):
        # expected status code == 422
        None

    def test_update_user(self, testapp):
        # update user bio using put call
        None
