# -*- coding: utf-8 -*-
from datetime import datetime
import re

SEQUENCE = 1

def nextId():
    """
    Return unique Int id near this tread
    :rtype: int
    """
    global SEQUENCE
    SEQUENCE += 1
    return SEQUENCE


class ManagerBase:
    def __init__(self, modelCls):
        #: :type: class
        self._modelCls = modelCls
        #: :type: modelCls
        self._objects = []

    def create(self, *args, **kwargs):
        self._objects.append(self._modelCls(*args, **kwargs))

    def add(self, user):
        self._objects.append(user)

    def filter(self, *args, **kwargs):
        tmp = []
        for user in self._objects:
            for arg in args:
                if arg(user):
                    tmp.append(user)
            for key, val in kwargs.items():
                if hasattr(user, key) and getattr(user, key) == val:
                    tmp.append(user)
        return tmp

    def find(self, *args, **kwargs):
        rsl = self.filter(*args, **kwargs)
        if rsl:
            return rsl.pop(0)

    def remove(self, *args, **kwargs):
        [self._objects.remove(i) for i in self.filter(*args, **kwargs)]

    def all(self):
        return self._objects

    def clear(self):
        self._objects = []


class User:
    #: :type: ManagerBase
    objects = None

    def __init__(self, email, name, password):
        self.id = nextId()
        self.session = ""
        self.email = email
        self.name = name
        self.password = password
        self.messages = []

    def sendTo(self, user, message):
        """
        :type user: User
        :type message: str
        """
        user = self.objects.find(name=user.name)
        user.messages.append(self, message)

    def __eq__(self, u):
        return self.name == u.name

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return '<User {0}>'.format(self.name)

User.objects = ManagerBase(User)


class Message:
    #: :type: ManagerBase
    objects = None

    def __init__(self, user, message):
        """
        :type user: User
        :type message: str
        """
        self.id = nextId()
        self.message = message
        self.owner = user
        user_names = re.findall(r'@(\w+)', message)
        self.users = [User.objects.find(name=n) for n in user_names]
        self.users_notify = [i for i in self.users]
        self.tags = re.findall(r'#(\w+)', message)
        self.time = datetime.now()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return '<Message {0}, "{1}">'.format(self.owner.name, self.message)

Message.objects = ManagerBase(Message)