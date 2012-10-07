# -*- coding: utf-8 -*-
import os
from glob import glob
from inspect import isclass
from threading import Thread
from tkinter import Button, Frame, Tk, messagebox
from unittest import TestLoader, TextTestRunner, TestSuite

import conf
from app.bottle import load, run
from tests.base import BaseSeleniumTest


class Application(Frame):
    test_status = False

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Selenium samples runner')
        self.master.wm_iconbitmap(default='app/static/favicon.ico')
        self.pack()
        self.createWidgets()
        self.start_server()

    def createWidgets(self):
        classes = self.get_tests_classes()

        all = lambda: self.run_tests(classes)
        btn_test_all = self.new_Button('Test all', all, 1)

        def _test(cls):
            return lambda: self.run_tests([cls])

        for i in range(len(classes)):
            cls = classes[i]
            name = self.get_class_name(cls)
            self.new_Button(name, _test(cls), i + 2)

    def new_Button(self, text, command, column):
        btn = Button(self, text=text, command=command)
        btn.config(width=8, height=2)
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
                        if isclass(cls) and cls != BaseSeleniumTest and issubclass(cls, BaseSeleniumTest):
                            tests.append(cls)
        return tests

    def start_server(self):
        def _server():
            load('app.controls')
            run(host=conf.SERVER_HOST, port=conf.SERVER_PORT)

        server = Thread(target=_server)
        server.setDaemon(True)
        server.start()

    def run_tests(self, testCls):
        def _tests(testCls):
            self.test_status = True
            with open(conf.RESULT_PATH, mode='w') as output:
                try:
                    suite = TestSuite()
                    for testCls in testCls:
                        subSuite = TestLoader().loadTestsFromTestCase(testCls)
                        suite.addTest(subSuite)

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
            Thread(target=_tests, args=[testCls, ]).start()


try:
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
except Exception as e:
    pass
