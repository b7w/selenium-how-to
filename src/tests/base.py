# -*- coding: utf-8 -*-

import unittest
import conf

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseSeleniumTest(unittest.TestCase):
    def setUp(self):
        """
        Запускается перед каждым вызовом метода теста
        """
        self.driver = webdriver.Firefox()
        # Неявное ожидание при поиске элементов, в случае если они не появились сразу же.
        self.driver.implicitly_wait(0.5)
        self.base_url = 'http://' + conf.SERVER

    def _find_element(self, func, id=None, xpath=None, cls=None, name=None, tag=None, css=None):
        if id:
            return func(by=By.ID, value=id)
        elif cls:
            return func(by=By.XPATH, value=cls)
        elif xpath:
            return func(by=By.CLASS_NAME, value=xpath)
        elif name:
            return func(by=By.NAME, value=name)
        elif tag:
            return func(by=By.TAG_NAME, value=tag)
        elif css:
            return func(by=By.CSS_SELECTOR, value=css)

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
        return self._find_element(self.driver.find_elements, **kwargs)

    def assertTitle(self, part):
        """
        Assert that `part` in self.driver.title.lower()
        """
        assert part in self.driver.title.lower()

    def is_present(self, **kwargs):
        """
        Wrapper for `driver.find_element` that catch NoSuchElementException
        """
        try:
            self.find(**kwargs)
        except NoSuchElementException:
            return False
        return True

    def send_post(self, input, button, data):
        """
        Clear `input` filed, set `data` and click `button`
        """
        self.driver.find_element_by_name(input).clear()
        self.driver.find_element_by_name(input).send_keys(data)
        self.driver.find_element_by_css_selector(button).click()

    def tearDown(self):
        """
        Запускается после каждого вызова метода теста
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
