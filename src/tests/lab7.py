# -*- coding: utf-8 -*-
import unittest

from tests.base import BaseSeleniumTestCase


class Lab7TestCase(BaseSeleniumTestCase):
    """
    Открыть http://yandex.ru/ и сравнить пересечение ссылок при поиске
    *эффективное тестирование программ* и *"эффективное тестирование"*
    """
    YANDEX = 'http://yandex.ru/yandsearch?p={page}&text={search}'

    name = 'Test lab 7'

    def test_search(self):
        text = 'эффективное тестирование программ'

        self.driver.get(self.YANDEX.format(page=0, search=text))
        self.assertTitle(text)

        query = self.find_all(css='.b-body-items li h2 a[href]')
        links = [link.get_attribute('href') for link in query]
        print(links)

        text2 = '"эффективное тестирование"'
        links2 = []
        for i in range(0, 3):
            self.driver.get(self.YANDEX.format(page=0, search=text2))
            self.assertTitle(text2)
            query = self.find_all(css='.b-body-items li h2 a[href]')
            links2.extend(link.get_attribute('href') for link in query)

        print(links2)

        both = list(set(links) & set(links2))
        print(both)
        assert len(both) == 1
        assert 'wikipedia' in both[0]

if __name__ == "__main__":
    unittest.main()
