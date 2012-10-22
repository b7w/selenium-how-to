# -*- coding: utf-8 -*-
from .import bottle
import re
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
    #TODO: REMOVE TEST HOOK
    #user_b7w.session = request.get_cookie(SESSION_NAME)
    user = get_user()
    if user is not None:
        count = len(Message.objects.filter(lambda m: user in m.users_notify))
        msgs = Message.objects.filter(lambda m: user in m.users, owner=user)
        return template('lab3logged', dict(user=user, messages=msgs, newsCount=count))
    else:
        return template('lab3', {})


@route('/lab3/message/create/', method='POST')
def lab3post():
    user = get_user()
    if user is not None:
        message = request.POST['message']
        if message:
            Message.objects.create(user, message)
        redirect('/lab3/')
    else:
        redirect('/lab3/login/')


@route('/lab3/message/<type>/<id>/', method='GET')
def lab3get(type, id):
    """
    :type type: str
    """
    user = get_user()
    id = int(id)
    if user is not None:
        if type == 'read':
            Message.objects.find(id=id).users_notify.remove(user)
        elif type == 'remove':
            Message.objects.remove(id=id)
        redirect('/lab3/')
    else:
        redirect('/lab3/login/')


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
    return dict(email='', username='', errors=[])


@route('/lab3/signup/', method='POST')
@view('lab3signup')
def lab3signup():
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    errors = []
    if not email or not re.match(r'^\w{3,12}@\w{3,8}\.\w{2,3}$', email):
        errors.append('Invalid email')
    if not username or not re.match(r'^\w{3,8}$', username):
        errors.append('Username - 3 latin characters or number')
    if not password or len(password) < 8:
        errors.append('Password - 8 characters')
    if User.objects.find(name=username):
        errors.append('Such user already registered')
    if not errors:
        User.objects.create(email, username, password)
        redirect("/lab3/login/")
    return dict(email=email, username=username, errors=errors)

#TODO: remove debug data
user_test = User('', 'Test', 'pass')
user_test2 = User('', 'Test2', 'pass')
User.objects.add(user_test)
User.objects.add(user_test2)
Message.objects.create(user_test, "Some message #tag #new")
Message.objects.create(user_test2, "One more message #post @Test")