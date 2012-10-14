# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver.support.select import Select

from tests.base import BaseSeleniumTest


class Lab2Test(BaseSeleniumTest):
    name = 'Test lab 2'

    def test_input1(self):
        """
        Test text input and checkbox
        """
        # Open FireFox and Load page
        self.driver.get(self.base_url + '/lab2/')
        self.assertTitle('lab 2')

        in1 = self.find(name='in1')
        in2 = self.find(name='in2')

        in1.clear()
        in1.send_keys('B')
        self.assertProgress('progress1', 20)

        # check that progress is clearing too
        self.find(name='in1').clear()
        self.assertProgress('progress1', 0)

        # clear text and check that value increase on each char
        # except spaces
        in1.clear()
        in1.send_keys('B7')
        self.assertProgress('progress1', 40)
        in1.send_keys('W')
        self.assertProgress('progress1', 60)
        in1.send_keys(' ')
        self.assertProgress('progress1', 60)
        in1.send_keys('2')
        self.assertProgress('progress1', 100)
        in1.send_keys('3')
        self.assertProgress('progress1', 100)

        assert not in2.get_attribute('checked')
        in2.click()
        assert in2.get_attribute('checked')

        self.assertButtonDisabled()

    def test_select(self):
        """
        Test select and malty select
        """
        # Open FireFox and Load page
        self.driver.get(self.base_url + '/lab2/')
        self.assertTitle('lab 2')

        in3 = Select(self.find(name='in3'))
        in4 = Select(self.find(name='in4'))

        # check that progress return back
        in3.select_by_visible_text('2')
        self.assertProgress('progress2', 40)
        in3.select_by_visible_text('something')
        self.assertProgress('progress2', 0)

        # send data and check that it is saved
        in3.select_by_visible_text('3')
        in4.select_by_visible_text('1')
        self.assertProgress('progress2', 60)

        in4.select_by_visible_text('2')
        self.assertProgress('progress2', 80)

        # check that progress return back
        in4.deselect_by_visible_text('2')
        self.assertProgress('progress2', 60)

        in4.select_by_visible_text('2')
        in4.select_by_visible_text('3')
        self.assertProgress('progress2', 100)

        in4.select_by_visible_text('4')
        self.assertProgress('progress2', 100)

        self.assertButtonDisabled()

    def test_file_text(self):
        """
        Test file input and text area.
        """
        # Open FireFox and Load page
        self.driver.get(self.base_url + '/lab2/')
        self.assertTitle('lab 2')

        # test file input
        self.assertProgress('progress3', 0)
        in5 = self.find(name='in5')
        in5.send_keys('path')
        self.assertProgress('progress3', 100)

        # test text area
        in6 = self.find(name='in6')
        in6.send_keys('five!' * 10)
        self.assertProgress('progress4', 50)
        in6.send_keys('five!' * 2)
        self.assertProgress('progress4', 60)

        # check that progress return back
        in6.clear()
        self.assertProgress('progress4', 0)

        in6.send_keys('five!' * 32)
        self.assertProgress('progress4', 100)
        self.assertButtonDisabled()

    def fill_data(self):
        """
        Fill data to all inputs
        in1 = 'Black7White'
        in2 = click()
        in3 = ['4']
        in4 = ['4','5','6']
        in5 = 'path'
        in6 = 'five!' * 32
        """
        self.find(name='in1').send_keys('Black7White')
        self.find(name='in2').click()

        in3 = Select(self.find(name='in3'))
        in3.select_by_visible_text('4')

        in4 = Select(self.find(name='in4'))
        in4.select_by_visible_text('4')
        in4.select_by_visible_text('5')
        in4.select_by_visible_text('6')

        self.find(name='in5').send_keys('path')
        self.find(name='in6').send_keys('five!' * 32)

    def test_save(self):
        """

        """
        self.driver.get(self.base_url + '/lab2/')
        self.assertTitle('lab 2')

        # Fill data and send post
        self.fill_data()
        assert 'disabled' not in self.find(id='save').get_attribute('class')

        self.find(id='save').click()
        assert 'saved' in self.driver.page_source.lower()

    def test_cancel(self):
        """
        Add some data and than cancel it and check that all inputs are clean
        """
        self.driver.get(self.base_url + '/lab2/')
        self.assertTitle('lab 2')

        # Fill data and send post
        self.fill_data()

        self.find(id='cancel').click()
        # Page is changed so we need bind again
        in1 = self.find(name='in1')
        in2 = self.find(name='in2')
        in3 = Select(self.find(name='in3'))
        in4 = Select(self.find(name='in4'))
        in6 = self.find(name='in6')

        assert in1.get_attribute('value') == ''
        assert not in2.get_attribute('checked')
        assert in3.all_selected_options[0].text == 'something'
        assert in4.all_selected_options == []
        assert in6.text == ''

        for i in range(1, 4):
            self.assertProgress('progress{0}'.format(i), 0)

    def assertProgress(self, id, percent):
        """
        Check that '{percent}%' in style attribute of '#{id}' element
        """
        # we use not `value_of_css_property( 'width' )` because it return real size in pixels
        sb_str = '{0}%'.format(percent)
        assert sb_str in self.find(id=id).get_attribute('style')

    def assertButtonDisabled(self):
        """
        Check that 'disabled' class in '#save' button
        """
        assert 'disabled' in self.find(id='save').get_attribute('class')


if __name__ == '__main__':
    unittest.main()