# -*- coding: utf-8 -*-
from time import time
from uuid import uuid4
from app.bottle import response, request
from app.models import User

SESSION_NAME = 'session'

def authenticate(username, password):
    """
    :rtype: User
    """
    user = User.objects.find(name=username)
    if user and user.password == password:
        return user
    return None


def get_user():
    """
    :rtype: User
    """
    session = request.get_cookie(SESSION_NAME)
    if session:
        return User.objects.find(session=session)


def login(user):
    """
    :type user: User
    """
    user.session = uuid4().hex
    response.set_cookie(SESSION_NAME, user.session,
        expires=time() + ( 3600 * 24 * 365 ),
        path='/'
    )


def logout(user):
    """
    :type user: User
    """
    response.delete_cookie(SESSION_NAME, path='/')
    user.session = ""