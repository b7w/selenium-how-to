# -*- coding: utf-8 -*-
import os
from glob import glob
from inspect import isclass
from threading import Thread
from tkinter import Button, Frame, Tk, messagebox
from unittest import TestLoader, TextTestRunner, TestSuite

import conf
from app.bottle import load, run
from tests.base import BaseSeleniumTestCase


class Application(Frame):
    test_status = False

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Selenium samples runner')
        self.master.wm_iconbitmap(default='app/static/favicon.ico')
        self.pack()
        self.create_widgets()
        self.start_server()

    def create_widgets(self):
        classes = self.get_tests_classes()

        all_tests = lambda: self.run_tests(classes)
        self.add_button('Test all', all_tests, 1)

        def _test(cls):
            return lambda: self.run_tests([cls])

        for i, cls in enumerate(classes, 2):
            name = self.get_class_name(cls)
            self.add_button(name, _test(cls), i)

    def add_button(self, text, command, column):
        btn = Button(self, text=text, command=command)
        btn.config(height=2)
        btn.grid(row=1, column=column)
        return btn

    def import_tests(self):
        for file in glob('tests/*.py'):
            name = os.path.splitext(os.path.basename(file))[0]
            if name != 'base':
                __import__('tests.{0}'.format(name))

    def get_class_name(self, cls):
        if hasattr(cls, 'name'):
            return cls.name
        return cls.__name__

    def get_tests_classes(self):
        self.import_tests()
        m = __import__('tests')
        tests = []
        for module_name in dir(m):
            if not module_name.startswith('_') and module_name != 'base':
                test = getattr(m, module_name)
                for cls_name in dir(test):
                    if not cls_name.startswith('_'):
                        cls = getattr(test, cls_name)
                        if isclass(cls) and cls != BaseSeleniumTestCase and issubclass(cls, BaseSeleniumTestCase):
                            tests.append(cls)
        return tests

    def start_server(self):
        def _server():
            load('app.controls')
            run(host=conf.SERVER_HOST, port=conf.SERVER_PORT)

        server = Thread(target=_server)
        server.setDaemon(True)
        server.start()

    def run_tests(self, test_class):
        def _tests(test_cls):
            self.test_status = True
            with open(conf.RESULT_PATH, mode='w') as output:
                try:
                    suite = TestSuite()
                    for cls in test_cls:
                        sub_suite = TestLoader().loadTestsFromTestCase(cls)
                        suite.addTest(sub_suite)

                    TextTestRunner(stream=output, descriptions=True, verbosity=2, failfast=True).run(suite)
                except Exception as e:
                    print("Fatal error on test running: " + str(e))

            if conf.RESULT_ENABLE:
                path = os.path.abspath(conf.RESULT_PATH)
                path = 'start {0}'.format(path)
                os.system(path)
            self.test_status = False

        if self.test_status:
            messagebox.showwarning('Tests', 'Some tests already running, wait')
        else:
            Thread(target=_tests, args=[test_class, ]).start()


try:
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
except Exception as e:
    pass
