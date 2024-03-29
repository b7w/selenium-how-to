# -*- coding: utf-8 -*-

import unittest
import conf

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseSeleniumTestCase(unittest.TestCase):
    """
    You need to extend form this class. And it will be load to UI runner automatic.
    """
    name = 'Test name in UI'
    base_url = 'http://' + conf.SERVER_URL

    @classmethod
    def setUpClass(cls):
        """
        Run before testing
        """
        cls.driver = webdriver.Firefox()
        # waite if elements not found
        cls.driver.implicitly_wait(0.5)
        cls.driver.maximize_window()

    def setUp(self):
        """
        Run before test method call
        """
        pass

    def _find_element(self, func, id=None, xpath=None, cls=None, name=None, tag=None, css=None):
        try:
            if id:
                return func(by=By.ID, value=id)
            elif cls:
                return func(by=By.CLASS_NAME, value=cls)
            elif xpath:
                return func(by=By.XPATH, value=xpath)
            elif name:
                return func(by=By.NAME, value=name)
            elif tag:
                return func(by=By.TAG_NAME, value=tag)
            elif css:
                return func(by=By.CSS_SELECTOR, value=css)
        except NoSuchElementException:
            pass

    def find(self, **kwargs):
        """
        :rtype: selenium.webdriver.remote.webelement.WebElement
        """
        if len(kwargs) != 1:
            raise ValueError("Only one key argument allowed")
        return self._find_element(self.driver.find_element, **kwargs)

    def find_all(self, **kwargs):
        """
        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        """
        if len(kwargs) != 1:
            raise ValueError("Only one key argument allowed")
        return self._find_element(self.driver.find_elements, **kwargs) or []

    def assertTitle(self, part):
        """
        Assert that `part` in self.driver.title.lower() or None
        """
        assert part in self.driver.title.lower()

    def tearDown(self):
        """
        Run after test method call
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """
        Run after testing
        """
        cls.driver.quit()
