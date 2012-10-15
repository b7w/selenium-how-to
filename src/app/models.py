# -*- coding: utf-8 -*-
import re

class UserManager:
    def __init__(self):
        self.objects = []

    def add(self, *args, **kwargs):
        """
        :type user: User
        """
        self.objects.append(User(*args, **kwargs))

    def find(self, name=None, session=None):
        """
        :type name: str
        :type session: str
        :rtype: User
        """
        for user in self.objects:
            if name and user.name == name:
                return user
            if session and user.session == session:
                return user

    def all(self):
        """
        :rtype: list of User
        """
        return self.objects


class User:
    objects = UserManager()

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


class MessageManager:
    def __init__(self):
        self.objects = []

    def add(self, *args, **kwargs):
        """
        :type message: Message
        """
        self.objects.append(Message(*args, **kwargs))


class Message:
    objects = MessageManager()

    def __init__(self, user, message):
        """
        :type user: User
        :type message: str
        """
        self.message = message
        self.owner = user
        self.users = re.findall(r'#\w+', message)
        self.tags = re.findall(r'@\w+', message)

    def __repr__(self):
        return '<Message {0}, {0}>'.format(self.owner, self.message)