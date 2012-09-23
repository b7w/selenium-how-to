# -*- coding: utf-8 -*-

from selenium.webdriver import Firefox

driver = Firefox()
driver.get('http://ya.ru/')
driver.close()