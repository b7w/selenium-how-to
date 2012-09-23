# -*- coding: utf-8 -*-
from app import bottle
from app.bottle import route, run, static_file, view, redirect
import conf

bottle.TEMPLATE_PATH = ['app/views']


@route('/static/<path:path>')
def static(path):
    return static_file(path, root='app/static')


@route('/')
def index():
    return redirect('/lab1/')


@route('/lab1/')
@view('lab1')
def lab1():
    return {}


@route('/lab1/<name:re:\w+>/')
def lab1pages(name):
    return "<h1>You enter <span class=\"name\" style=\"color: red\">{name}</span> page</h1>".format(name=name)


@route('/lab2/')
@view('lab2')
def lab2():
    return {}


@route('/lab2/saved/')
def lab2saved():
    return "<h1>Saved</h1>"


@route('/lab3/')
@view('lab3')
def hello():
    return {}


@route('/about/')
@view('about')
def about():
    return {}

run(host=conf.SERVER_HOST, port=conf.SERVER_PORT, reloader=True, debug=True)