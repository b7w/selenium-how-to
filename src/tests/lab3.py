# -*- coding: utf-8 -*-

import unittest

from tests.base import BaseSeleniumTest


class Lab3Test(BaseSeleniumTest):
    name = 'Test lab 3'

    userFirst = 'B7W'
    userSecond = 'Keks'

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

        # check that fields saved
        self.find(id='email').send_keys('email@domain.ru')
        self.find(id='username').send_keys('Keks')
        self.find(id='submit').click()
        self.assertTitle('sign up')
        assert self.find(id='email').get_attribute('value') == 'email@domain.ru'
        assert self.find(id='username').get_attribute('value') == 'Keks'

        # check errors
        assert 'password' in self.find(id='errors').text.lower()

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
        self.driver.get(self.base_url + "/lab3/signup/")
        self.find(id='email').send_keys('email@domain.ru')
        self.find(id='username').send_keys(self.userFirst)
        self.find(id='password').send_keys('1a2b3c4d')
        self.find(id='submit').click()
        self.assertTitle('sign in')

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
