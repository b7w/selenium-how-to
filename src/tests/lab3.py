# -*- coding: utf-8 -*-

import unittest

from tests.base import BaseSeleniumTest


class Lab3Test(BaseSeleniumTest):
    def test_sum(self):
        """
        Test sum
        """
        self.driver.get(self.base_url + '/lab3/')
        self.assertTitle('lab 3')

        self.find(id='num7').click()
        self.assertText(7, 0)
        self.find(id='plus').click()
        self.assertText('', 7)
        self.find(id='num8').click()
        self.assertText(8, 7)
        self.find(id='equal').click()
        self.assertText(15, 7)
        self.find(id='plus').click()
        self.find(id='num5').click()
        self.find(id='point').click()
        self.find(id='num5').click()
        self.assertText(5.5, 15)
        self.find(id='equal').click()
        self.assertText(20.5, 15)


    def test_min(self):
        """
        Test min
        """
        self.driver.get(self.base_url + '/lab3/')
        self.assertTitle('lab 3')

        self.find(id='num1').click()
        self.find(id='num8').click()
        self.assertText(18, 0)
        self.find(id='min').click()
        self.assertText('', 18)
        self.find(id='num3').click()
        self.assertText(3, 18)
        self.find(id='equal').click()
        self.assertText(15, 18)
        self.find(id='min').click()
        self.find(id='num5').click()
        self.find(id='point').click()
        self.find(id='num5').click()
        self.assertText(5.5, 15)
        self.find(id='equal').click()
        self.assertText(9.5, 15)

    def test_mul(self):
        """
        Test mul
        """
        self.driver.get(self.base_url + '/lab3/')
        self.assertTitle('lab 3')

        self.find(id='num4').click()
        self.assertText(4, 0)
        self.find(id='mul').click()
        self.assertText('', 4)
        self.find(id='num6').click()
        self.assertText(6, 4)
        self.find(id='equal').click()
        self.assertText(24, 4)
        self.find(id='mul').click()
        self.assertText('', 24)
        self.find(id='num0').click()
        self.find(id='point').click()
        self.find(id='num5').click()
        self.assertText(0.5, 24)
        self.find(id='equal').click()
        self.assertText(12, 24)

    def test_del(self):
        """
        Test del
        """
        self.driver.get(self.base_url + '/lab3/')
        self.assertTitle('lab 3')

        self.find(id='num1').click()
        self.find(id='num5').click()
        self.assertText(15, 0)
        self.find(id='del').click()
        self.assertText('', 15)
        self.find(id='num5').click()
        self.assertText(5, 15)
        self.find(id='equal').click()
        self.assertText(3, 15)
        self.find(id='del').click()
        self.assertText('', 3)
        self.find(id='num0').click()
        self.find(id='point').click()
        self.find(id='num5').click()
        self.assertText(0.5, 3)
        self.find(id='equal').click()
        self.assertText(6, 3)

    def test_clear(self):
        """
        Test clear
        """
        self.driver.get(self.base_url + '/lab3/')
        self.assertTitle('lab 3')

        self.find(id='num3').click()
        self.find(id='num5').click()
        self.assertText(35, 0)
        self.find(id='mul').click()
        self.assertText('', 35)
        self.find(id='clear').click()
        self.assertText('', 0)
        self.find(id='num1').click()
        self.assertText(1, 0)
        self.find(id='plus').click()
        self.assertText('', 1)
        self.find(id='num2').click()
        self.assertText(2, 1)
        self.find(id='equal').click()
        self.assertText(3, 1)


    def assertText(self, first, second):
        assert self.find(id='text').get_attribute('value') == str(first)
        assert self.find(id='buffer').text == str(second)

if __name__ == '__main__':
    unittest.main()
