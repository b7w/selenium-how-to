# -*- coding: utf-8 -*-
import unittest

from tests.base import BaseSeleniumTestCase


class Lab6TestCase(BaseSeleniumTestCase):
    """
    Открыть http://www.artlebedev.ru/tools/case/ и проверить
    два текстовых поля, радио кнопки, кнопку очистки.
    """
    name = 'Test lab 6'

    def test_case(self):
        self.driver.get('http://www.artlebedev.ru/tools/case/')
        self.assertTitle('конвертер')
        text = 'Очень необычный ТЕКСТ'
        self.find(name='source').send_keys(text)

        # Верхний регистр
        self.find(id='Method0').click()
        assert self.find(name='target').get_attribute('value') == text.upper()

        # Нижний регистр
        self.find(id='Method1').click()
        assert self.find(name='target').get_attribute('value') == text.lower()

        # Все слова перевести в нижний регистр и
        # сделать первую букву каждого слова заглавной
        self.find(id='Method2').click()
        tmp = ' '.join(word.capitalize() for word in text.split())
        assert self.find(name='target').get_attribute('value') == tmp

        # Инверсия регистра
        self.find(id='Method3').click()
        assert self.find(name='target').get_attribute('value') == text.swapcase()

        # Очистка полей
        self.find(css='input[type=reset]').click()
        assert self.find(name='source').get_attribute('value') == ''
        assert self.find(name='target').get_attribute('value') == ''


if __name__ == "__main__":
    unittest.main()
