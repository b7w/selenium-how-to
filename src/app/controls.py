# -*- coding: utf-8 -*-
from .import bottle
from app.models import User, Message
from app.utils import authenticate, logout, login, SESSION_NAME, redirect, get_user
from .bottle import route, static_file, view, request, template

bottle.TEMPLATE_PATH = ['app/views']


@route('/static/<path:path>')
def static(path):
    """
    Serve static files
    """
    return static_file(path, root='app/static')


@route('/')
def index():
    """
    Redirect from root to first lab
    """
    return redirect('/lab1/')


@route('/about/')
@view('about')
def about():
    """
    About page
    """
    return {}

#
# Routes for lab 1
#
@route('/lab1/')
@view('lab1')
def lab1():
    return {}


@route('/lab1/<name:re:\w+>/')
def lab1pages(name):
    return "<h1>You enter <span class=\"name\" style=\"color: red\">{name}</span> page</h1>".format(name=name)


#
# Routes for lab 2
#
@route('/lab2/')
@view('lab2')
def lab2():
    return {}


@route('/lab2/saved/')
def lab2saved():
    return "<h1>Saved</h1>"


#
# Routes for lab 3
#
@route('/lab3/')
@view('lab3')
def lab3():
    user = get_user()
    if user is not None:
        m = Message.objects._objects
        return template('lab3logged', dict(messages=m))
    else:
        return template('lab3', {})


@route('/lab3/post/', method='POST')
def lab3post():
    user = get_user()
    if user is not None:
        message = request.POST['message']
        Message.objects.create(user, message)
    redirect('/lab3/')


@route('/lab3/login/')
@view('lab3login')
def lab3login():
    if get_user():
        redirect('/lab3/')
    return dict(username='', error=False)


@route('/lab3/login/', method='POST')
@view('lab3login')
def lab3login():
    username = request.POST['username']
    password = request.POST['password']
    error = False
    user = authenticate(username, password)
    if user:
        login(user)
        redirect('/lab3/')
    else:
        error = True
    return dict(username=username, error=error)


@route('/lab3/logout/')
def lab3logout():
    session = request.get_cookie(SESSION_NAME)
    if session:
        user = User.objects.find(session=session)
        if user:
            logout(user)
    redirect('/lab3/')


@route('/lab3/signup/')
@view('lab3signup')
def lab3signup():
    if get_user():
        redirect('/lab3/')
    return dict(email='', username='', error='')


@route('/lab3/signup/', method='POST')
@view('lab3signup')
def lab3signup():
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    error = False
    if email and username and password:
        if not User.objects.find(name=username):
            User.objects.create(email, username, password)
            redirect("/lab3/login/")
    else:
        error = True
    return dict(email=email, username=username, error=error)

#TODO: remove debug data
user_b7w = User('', 'B7W', 'pass')
user_test = User('', 'Test', 'pass')
User.objects.add(user_b7w)
User.objects.add(user_test)
Message.objects.create(user_b7w, "Some message #tag #new @B7W")
Message.objects.create(user_test, "One more message #post #null @None")