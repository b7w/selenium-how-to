# -*- coding: utf-8 -*-
import unittest
from urllib.parse import urlsplit
from http.client import HTTPConnection

from tests.base import BaseSeleniumTestCase


class Example1TestCase(BaseSeleniumTestCase):
    """
    Для первого примера давайте найдем все ссылки из колонок на странице "Example 1" и перейдем по ним.
    Это все блоки помечены цветом, плюс кнопки.
    А так же проверим что текст ссылки присутствует на открытых страницах.
    """
    name = 'Test example 1'

    def test_follow_links(self):
        """
        Find all links ( 'a' tag ) with href attribute,
        Get this links.
        """
        self.driver.get(self.base_url + '/example1/')
        self.assertTitle('example 1')

        elements = self.find_all(css='.row-fluid a[href]')
        links = []
        for item in elements:
            href = item.get_attribute('href')
            links.append((item.text.lower(), href))

        assert len(links) == 9, len(links)
        for text, href in links:
            self.driver.get(href)
            source = self.driver.page_source.lower()
            for word in text.split():
                assert word in source
            assert self.find(css='span.name').text.lower() == text.replace(' ', '')

    def test_resource(self):
        """
        Check http status code of all css, js, img resources on a page
        """
        self.driver.get(self.base_url + '/example1/')
        self.assertTitle('example 1')

        for item in self.find_all(css='link[href]'):
            assert self.http_status(item.get_attribute("href")) == 200

        for item in self.find_all(css='script[src]'):
            assert self.http_status(item.get_attribute("src")) == 200

        for item in self.find_all(css='img[src]'):
            assert self.http_status(item.get_attribute("src")) == 200

        for item in self.find_all(css='a[href]'):
            link = item.get_attribute('href')
            if link.startswith('http:'):
                assert self.http_status(link) == 200

    def http_status(self, url):
        """
        Make HTTPConnection to the server send GET request and return status.
        Url is parsed with urlsplit.
        """
        host = urlsplit(url)
        conn = HTTPConnection(host.netloc, timeout=8)
        conn.request('HEAD', host.path)
        res = conn.getresponse()
        return res.status

if __name__ == "__main__":
    unittest.main()
