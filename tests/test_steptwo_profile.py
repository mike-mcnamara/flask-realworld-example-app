# coding: utf-8

from flask import url_for
from conduit.exceptions import USER_NOT_FOUND


def _register_user(testapp, **kwargs):
    return testapp.post_json(url_for('user.register_user'), {
          "user": {
              "email": 'foo@bar.com',
              "username": 'foobar',
              "password": 'myprecious'
          }}, **kwargs)


class TestProfile:

    None
