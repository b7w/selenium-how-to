# -*- coding: utf-8 -*-

import unittest

from tests.base import BaseSeleniumTest


class Lab3Test(BaseSeleniumTest):
    name = 'Test lab 3'

    USER_FIRST = 'B7W'
    USER_SECOND = 'Keks'
    PASSWORD = '1a2b3c4d'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver.get(cls.base_url + '/lab3/db/dump/')
        cls.driver.get(cls.base_url + '/lab3/db/clear/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.get(cls.base_url + '/lab3/db/load/')
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.driver.get(self.base_url + '/lab3/db/clear/')

    def test_privet_urls(self):
        """
        Test url that accessible only if you authenticated
        """
        self.driver.get(self.base_url + '/lab3/')
        self.assertTitle('lab 3')
        assert len(self.find_all(cls='btn')) == 2
        assert self.find(id='user-info') is None

        self.driver.get(self.base_url + '/lab3/message/read/1/')
        self.assertTitle('lab 3')

        self.driver.get(self.base_url + '/lab3/message/remove/1/')
        self.assertTitle('lab 3')


    def test_sign_up(self):
        """
        Test various sign up data and out messages.
        Add new user.
        """
        self.driver.get(self.base_url + "/lab3/signup/")
        self.assertTitle('sign up')

        # check clear fields errors
        self.find(id='submit').click()
        assert 'email' in self.find(id='errors').text.lower()
        assert 'username' in self.find(id='errors').text.lower()
        assert 'password' in self.find(id='errors').text.lower()

        # check that fields saved
        self.find(id='email').send_keys('email@domain.ru')
        self.find(id='username').send_keys('Keks')
        self.find(id='submit').click()
        self.assertTitle('sign up')
        assert self.find(id='email').get_attribute('value') == 'email@domain.ru'
        assert self.find(id='username').get_attribute('value') == 'Keks'

        # check field errors
        self.assertFieldErrors('email', 'email@d.s')
        self.assertFieldErrors('email', 'email@domain.long')
        self.assertFieldErrors('email', '$email%dom.ru')
        self.assertFieldErrors('email', 'email_too_long@dom.ru')

        self.assertFieldErrors('username', 'BW')
        self.assertFieldErrors('username', 'B&W')
        self.assertFieldErrors('username', 'B7W' * 8)

        self.assertFieldErrors('password', '123')

        # new user
        self.registerUser(self.USER_FIRST + '@ya.ru', self.USER_FIRST, self.PASSWORD)
        self.assertTitle('sign in')
        self.registerUser(self.USER_FIRST + '@ya.ru', self.USER_FIRST, self.PASSWORD)
        self.assertTitle('sign up')
        assert 'already registered' in self.find(id='errors').text.lower()

    def test_login(self):
        """
        Test auth and out messages
        """
        self.driver.get(self.base_url + '/lab3/login/')
        self.assertTitle('sign in')

        # check clear fields error
        self.find(id='submit').click()
        self.assertTitle('sign in')
        assert 'username' in self.find(id='errors').text.lower()
        assert 'password' in self.find(id='errors').text.lower()

        # check that fields saved
        self.loginUser(self.USER_FIRST, 'wrong')
        self.assertTitle('sign in')
        assert self.find(id='username').get_attribute('value') == self.USER_FIRST
        assert self.find(id='password').get_attribute('value') == ''

        # check error message
        assert 'incorrect' in self.find(id='errors').text.lower()

        self.registerUser(self.USER_FIRST + '@ya.ru', self.USER_FIRST, self.PASSWORD)
        self.assertTitle('sign in')
        self.loginUser(self.USER_FIRST, self.PASSWORD)
        self.assertTitle('home')

        assert self.find(css='.user-name strong').text == self.USER_FIRST
        self.find(id='logout').click()
        assert self.find(id='user-info') is None

    def test_add_message(self):
        """
        Test posting for yourself, test tags.
        """
        # make new user
        self.registerUser(self.USER_FIRST + '@ya.ru', self.USER_FIRST, self.PASSWORD)
        self.assertTitle('sign in')
        self.loginUser(self.USER_FIRST, self.PASSWORD)
        self.assertTitle('home')

        # add 2 posts
        self.find(id='post').send_keys('First message #tag1')
        self.find(id='submit').click()
        self.find(id='post').send_keys('Second message #tag1 #tag2')
        self.find(id='submit').click()

        # check count, unzip and check text
        assert len(self.find_all(cls='message')) == 2
        first, second = self.find_all(cls='message-body')
        assert first.text == 'First message #tag1'
        assert second.text == 'Second message #tag1 #tag2'

        # check correct user from
        first, second = self.find_all(css='.message .user-from')
        assert first.text == 'Mine'
        assert second.text == 'Mine'

        # get messages #id and check tags count and text
        first, second = self.find_all(cls='message')
        css = '#{id} .tags .badge'.format(id=first.get_attribute('id'))
        assert len(self.find_all(css=css)) == 1
        assert self.find(css=css).text == 'tag1'

        css = '#{id} .tags .badge'.format(id=second.get_attribute('id'))
        assert len(self.find_all(css=css)) == 2
        tag1, tag2 = self.find_all(css=css)
        assert tag1.text == 'tag1'
        assert tag2.text == 'tag2'

    def test_message_notification(self):
        """
        Test message posting between users.
        Set message as read. Delete message.
        """
        # make 2 new users
        self.registerUser(self.USER_FIRST + '@ya.ru', self.USER_FIRST, self.PASSWORD)
        self.assertTitle('sign in')
        self.registerUser(self.USER_SECOND + '@ya.ru', self.USER_SECOND, self.PASSWORD)
        self.assertTitle('sign in')

        self.loginUser(self.USER_FIRST, self.PASSWORD)
        self.assertTitle('home')

        # send post to second user
        hello = 'Hello @{user}'.format(user=self.USER_SECOND)
        self.find(id='post').send_keys(hello)
        self.find(id='submit').click()

        # login second user
        self.find(id='logout').click()
        assert self.find(id='user-info') is None
        self.loginUser(self.USER_SECOND, self.PASSWORD)
        self.assertTitle('home')

        # notification count and message
        assert self.find(css='#user-info .badge').text == '1'
        assert len(self.find_all(cls='message')) == 1
        assert self.find(cls='message-body').text == hello
        assert self.find(css='.message .user-from').text == self.USER_FIRST

        # set message as read
        self.find(css='.message .icon-ok').click()
        assert self.find(css='#user-info .badge') is None
        assert len(self.find_all(cls='message')) == 1

        # remove message
        self.find(css='.message .icon-remove').click()
        assert len(self.find_all(cls='message')) == 0

    def registerUser(self, email, username, password):
        """
        Feel data on 'sign up' page and click 'submit'
        """
        self.driver.get(self.base_url + '/lab3/signup/')
        self.find(id='email').send_keys(email)
        self.find(id='username').send_keys(username)
        self.find(id='password').send_keys(password)
        self.find(id='submit').click()

    def loginUser(self, username, password):
        """
        Feel data on 'sign in' page and click 'submit'
        """
        self.driver.get(self.base_url + '/lab3/login/')
        self.find(id='username').send_keys(username)
        self.find(id='password').send_keys(password)
        self.find(id='submit').click()

    def assertFieldErrors(self, filed_id, data):
        """
        Clear and send `data to `filed_id`, submit.
        Assert that #errors have `filed_id` in body
        """
        self.find(id=filed_id).clear()
        self.find(id=filed_id).send_keys(data)
        self.find(id='submit').click()
        self.assertTitle('sign up')
        assert filed_id in self.find(id='errors').text.lower()


if __name__ == '__main__':
    unittest.main()
