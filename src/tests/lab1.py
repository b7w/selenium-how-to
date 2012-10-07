# -*- coding: utf-8 -*-
import unittest
from urllib.parse import urlsplit
from http.client import HTTPConnection

from tests.base import BaseSeleniumTest


class Lab1Test(BaseSeleniumTest):
    name = 'Test lab 1'

    def test_follow_links(self):
        """
        Find all links ( 'a' tag ) with href attribute,
        filter with regex for .../lab1/.../
        Get this links.
        """
        self.driver.get(self.base_url + "/lab1/")
        self.assertTitle('lab 1')

        elements = self.find_all(css=".row-fluid a[href]")
        links = []
        for item in elements:
            href = item.get_attribute("href")
            links.append((item.text, href))

        assert len(links) == 9, len(links)
        for text, href in links:
            self.driver.get(href)
            for word in text.split():
                assert word.lower() in self.driver.page_source.lower()
            assert self.find(css="span.name").text == text.lower().replace(' ', '')

    def test_resource(self):
        """
        Check http status code of all css, js, img resources on a page
        """
        self.driver.get(self.base_url + "/lab1/")
        self.assertTitle('lab 1')

        for item in self.find_all(css="link[href]"):
            assert self.http_status(item.get_attribute("href")) == 200

        for item in self.find_all(css="script[src]"):
            assert self.http_status(item.get_attribute("src")) == 200

        for item in self.find_all(css="img[src]"):
            assert self.http_status(item.get_attribute("src")) == 200

        for item in self.find_all(css="a[href]"):
            link = item.get_attribute("href")
            if link.startswith('http:'):
                assert self.http_status(link) == 200

    def http_status(self, url):
        """
        Make HTTPConnection to the server send GET request and return status.
        Url is parsed with urlsplit.
        """
        host = urlsplit(url)
        conn = HTTPConnection(host.netloc, timeout=8)
        conn.request("GET", host.path)
        res = conn.getresponse()
        return res.status

if __name__ == "__main__":
    unittest.main()
