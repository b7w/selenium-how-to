# -*- coding: utf-8 -*-

import unittest

from tests.base import BaseSeleniumTest


class Lab3Test(BaseSeleniumTest):
    name = 'Test lab 3'

    USER_FIRST = 'B7W'
    USER_SECOND = 'Keks'
    PASSWORD = '1a2b3c4d'

    def setUp(self):
        super().setUp()
        self.driver.get(self.base_url + "/lab3/clear/")

    def test_privet_urls(self):
        """
        Test url that accessible only if you authenticated
        """
        self.driver.get(self.base_url + "/lab3/")
        self.assertTitle('lab 3')
        assert len(self.find_all(css=".btn")) == 2
        assert self.find(id="user-info") is None

        self.driver.get(self.base_url + "/lab3/message/read/1/")
        self.assertTitle('lab 3')

        self.driver.get(self.base_url + "/lab3/message/remove/1/")
        self.assertTitle('lab 3')


    def test_sign_up(self):
        """
        Test various sign up data and out messages
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
        self.assertFieldErrors('email', 'email@dom.s')
        self.assertFieldErrors('email', 'email@dom.long')
        self.assertFieldErrors('email', '$email@dom.ru')
        self.assertFieldErrors('email', 'email_too_long@dom.ru')

        self.assertFieldErrors('username', 'BW')
        self.assertFieldErrors('username', 'B&W')
        self.assertFieldErrors('username', 'B7W' * 4)

        self.assertFieldErrors('password', '123')
        self.assertFieldErrors('password', '123456')

        # new user
        self.registerUser(self.USER_FIRST + '@ya.ru', self.USER_FIRST, self.PASSWORD)
        self.assertTitle('sign in')
        self.registerUser(self.USER_FIRST + '@ya.ru', self.USER_FIRST, self.PASSWORD)
        self.assertTitle('sign up')
        assert 'already registered' in self.find(id='errors').text.lower()

    def test_login(self):
        """

        """
        self.driver.get(self.base_url + "/lab3/login/")
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

        assert 'password' in self.find(id='errors').text.lower()

        self.registerUser(self.USER_FIRST + '@ya.ru', self.USER_FIRST, self.PASSWORD)
        self.assertTitle('sign in')
        self.loginUser(self.USER_FIRST, self.PASSWORD)
        self.assertTitle('home')

    def registerUser(self, email, username, password):
        """
        Feel data on 'sign up' page and click 'submit'
        """
        self.driver.get(self.base_url + "/lab3/signup/")
        self.find(id='email').send_keys(email)
        self.find(id='username').send_keys(username)
        self.find(id='password').send_keys(password)
        self.find(id='submit').click()

    def loginUser(self, username, password):
        """
        Feel data on 'sign in' page and click 'submit'
        """
        self.find(id='username').send_keys(username)
        self.find(id='password').send_keys(password)
        self.find(id='submit').click()

    def assertFieldErrors(self, filed, data):
        """
        Clear and send `data to `field`, submit.
        Assert that #errors have `field` in body
        """
        self.find(id=filed).clear()
        self.find(id=filed).send_keys(data)
        self.find(id='submit').click()
        self.assertTitle('sign up')
        assert filed in self.find(id='errors').text.lower()

    def test_(self):
        """

        """

if __name__ == '__main__':
    unittest.main()
