# -*- coding: utf-8 -*-
from datetime import datetime
import re

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

    def find(self, **kwargs):
        for user in self._objects:
            for key, val in kwargs.items():
                if hasattr(user, key) and getattr(user, key) == val:
                    return user

    def filter(self, **kwargs):
        tmp = []
        for user in self._objects:
            for key, val in kwargs.items():
                if hasattr(user, key) and getattr(user, key) == val:
                    tmp.append(user)
        return tmp

    def all(self):
        return self._objects


class User:
    #: :type: ManagerBase
    objects = None

    def __init__(self, email, name, password):
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
        self.message = message
        self.owner = user
        self.users = re.findall(r'@(\w+)', message)
        self.tags = re.findall(r'#(\w+)', message)
        self.time = datetime.now()

    def __repr__(self):
        return '<Message {0}, "{1}">'.format(self.owner.name, self.message)

Message.objects = ManagerBase(Message)