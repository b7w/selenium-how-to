# -*- coding: utf-8 -*-
import re
import unittest
import http
import urllib

from tests.base import BaseSeleniumTest


class Lab1Test(BaseSeleniumTest):
    def test_follow_links(self):
        """
        Find all links ( 'a' tag ) with href attribute,
        filter with regex for .../lab1/.../
        Get this links.
        """
        self.driver.get(self.base_url + "/lab1/")
        assert "lab 1" in self.driver.title.lower()

        all_a = self.find_all(css="a[href]")
        lab_a_links = []
        for item in all_a:
            href = item.get_attribute("href")
            if re.match(".*/lab1/\w+/$", href):
                lab_a_links.append((item.text, href))

        assert len(lab_a_links) == 9, len(lab_a_links)
        for text, href in lab_a_links:
            self.driver.get(href)
            for word in text.split():
                assert word.lower() in self.driver.page_source.lower()
            assert self.find(css="span.name").text == text.lower().replace(' ', '')

    def test_resource(self):
        """
        Check http status code of all css, js, img resources on a page
        """
        self.driver.get(self.base_url + "/lab1/")
        assert "lab 1" in self.driver.title.lower()

        for item in self.find_all(css="link[href]"):
            assert self.http_status(item.get_attribute("href")) == 200

        for item in self.find_all(css="script[src]"):
            assert self.http_status(item.get_attribute("src")) == 200

        for item in self.find_all(css="img[src]"):
            assert self.http_status(item.get_attribute("src")) == 200

        for item in self.find_all(css="a[href]"):
            assert self.http_status(item.get_attribute("href")) == 200

    def http_status(self, url):
        """
        Make httplib.HTTPConnection to the server send GET request and return status.
        Url is parsed with urlparse.urlparse
        """
        host = urllib.parse(url)
        conn = http.client.HTTPConnection(host.netloc)
        conn.request("GET", host.path)
        res = conn.getresponse()
        return res.status

if __name__ == "__main__":
    unittest.main()
