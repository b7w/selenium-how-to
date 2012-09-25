# -*- coding: utf-8 -*-
import os
import subprocess
from threading import Thread
from tkinter import Button, Frame, Tk, messagebox, W, E, N, S
from unittest import TestLoader, TextTestRunner, TestSuite

import conf
from tests.lab1 import Lab1Test
from tests.lab2 import Lab2Test
from tests.lab3 import Lab3Test


class Application(Frame):
    server_status = False
    server_process = None

    test_status = False

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Selenium samples runner')
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.btn_server = self.new_Button('Start server', self.on_btn_server)
        self.btn_server.config()
        self.btn_server.grid(row=1, column=1, columnspan=4, sticky=W + E + N + S)

        self.btn_test_all = self.new_Button('Test all', self.on_btn_test_all)
        self.btn_test_all.grid(row=2, column=1)

        self.btn_test_lab1 = self.new_Button('Test lab 1', self.on_btn_test_lab1)
        self.btn_test_lab1.grid(row=2, column=2)

        self.btn_test_lab2 = self.new_Button('Test lab 2', self.on_btn_test_lab2)
        self.btn_test_lab2.grid(row=2, column=3)

        self.btn_test_lab3 = self.new_Button('Test lab 3', self.on_btn_test_lab3)
        self.btn_test_lab3.grid(row=2, column=4)

    def new_Button(self, text, command):
        btn = Button(self, text=text, command=command)
        btn.config(width=8, height=2)
        return btn

    def server_start(self):
        if not os.path.lexists(conf.PYTHON_PATH):
            messagebox.showerror('Error', 'Not found python. Install it or check PYTHON_PATH in conf.py')
            raise EnvironmentError("No found " + conf.PYTHON_PATH)
        print('Start http server')
        self.server_status = True
        path = os.path.abspath('server.py')
        self.server_process = subprocess.Popen('{0} {1}'.format(conf.PYTHON_PATH, path))
        self.btn_server.config(text='Stop server')

    def server_stop(self):
        if self.test_status:
            messagebox.showwarning('Tests', 'Some tests already running, wait')
        else:
            print('Stop http server')
            self.server_status = False
            self.server_process.kill()
            self.btn_server.config(text='Start server')

    def on_btn_server(self):
        try:
            if self.server_status:
                self.server_stop()
            else:
                self.server_start()
        except Exception as e:
            print("Fatal error on running server: " + str(e))

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
                    if not self.server_status:
                        self.server_start()
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
