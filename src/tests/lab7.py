# -*- coding: utf-8 -*-
import unittest

from tests.base import BaseSeleniumTestCase


class Lab7TestCase(BaseSeleniumTestCase):
    """
    Открыть http://rambler.ru/ и сравнить поиск
    """
    name = 'Test lab 7'

    def test_search(self):
        text = 'эффективное тестирование программ'
        self.driver.get('http://yandex.ru/')
        self.assertTitle('яндекс')
        self.find(id='text').send_keys(text)
        self.find(css='.arr input[type=submit]').click()
        links = [l.get_attribute('href') for l in self.find_all(css='.b-body-items li h2 a[href]')]
        print(links)

    def test_test(self):
        self.driver.get('http://yandex.ru/yandsearch?text=%D1%8D%D1%84%D1%84%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5+%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC&lr=213')
        print(self.find(xpath='a[text()="2"'))

if __name__ == "__main__":
    unittest.main()
