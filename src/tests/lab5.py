# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

from tests.base import BaseSeleniumTestCase

class Tab:
    """
    Класс для хранения ссылки, которая открывается в новом окне.
    После чего подсчитывается количество вхождений слова "nAble".
    """

    def __init__(self, link):
        self.link = link
        self.tab = webdriver.Firefox()
        self.tab.get(link)
        self.count = self.tab.page_source.count('nAble')

    def close(self):
        self.tab.close()

    def __str__(self):
        return "Tab{{{0}, {1}}}".format(self.count, self.link)


class Lab5TestCase(BaseSeleniumTestCase):
    """
    Открыть http://www.siaxx.com/ открыть все ссылки и посчитать кол вхождений "nAble".
    Закрыть ссылки в порядке увывания кол вхождений слова.
    """
    name = 'Test lab 5'

    def test_links(self):
        self.driver.get('http://www.siaxx.com/')
        self.assertTitle('siaxx')

        elements = self.find_all(css='a[href]')
        links = []
        for item in elements[1:4]:
            href = item.get_attribute('href')
            links.append(Tab(href))

        print(len(links))
        for tab in sorted(links, key=lambda x: x.count, reverse=True):
            print(tab)
            tab.close()

if __name__ == "__main__":
    unittest.main()
