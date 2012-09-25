# -*- coding: utf-8 -*-
import os
from threading import Thread
from tkinter import Button, Frame, Tk, messagebox
from unittest import TestLoader, TextTestRunner, TestSuite
from app.bottle import load, run

import conf
from tests.lab1 import Lab1Test
from tests.lab2 import Lab2Test
from tests.lab3 import Lab3Test


class Application(Frame):
    test_status = False

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Selenium samples runner')
        self.pack()
        self.createWidgets()
        self.start_server()

    def createWidgets(self):
        self.btn_test_all = self.new_Button('Test all', self.on_btn_test_all)
        self.btn_test_all.grid(row=1, column=1)

        self.btn_test_lab1 = self.new_Button('Test lab 1', self.on_btn_test_lab1)
        self.btn_test_lab1.grid(row=1, column=2)

        self.btn_test_lab2 = self.new_Button('Test lab 2', self.on_btn_test_lab2)
        self.btn_test_lab2.grid(row=1, column=3)

        self.btn_test_lab3 = self.new_Button('Test lab 3', self.on_btn_test_lab3)
        self.btn_test_lab3.grid(row=1, column=4)

    def new_Button(self, text, command):
        btn = Button(self, text=text, command=command)
        btn.config(width=8, height=2)
        return btn

    def start_server(self):
        def _server():
            load('app.controls')
            run(host=conf.SERVER_HOST, port=conf.SERVER_PORT)

        server = Thread(target=_server)
        server.setDaemon(True)
        server.start()

    def on_btn_test_lab1(self):
        self.run_tests([Lab1Test])

    def on_btn_test_lab2(self):
        self.run_tests([Lab1Test])

    def on_btn_test_lab3(self):
        self.run_tests([Lab1Test])

    def on_btn_test_all(self):
        self.run_tests([Lab1Test, Lab2Test, Lab3Test])

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
