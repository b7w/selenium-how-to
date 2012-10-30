# -*- coding: utf-8 -*-
from .import bottle
import re
from app.models import User, Message
from app.utils import authenticate, logout, login, SESSION_NAME, redirect, get_user
from .bottle import route, static_file, view, request, template, abort

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
    Redirect from root to first example
    """
    return redirect('/example1/')


@route('/about/')
@view('about')
def about():
    """
    About page
    """
    return {}

#
# Routes for example 1
#
@route('/example1/')
@view('example1')
def example1():
    return {}


@route('/example1/<name:re:\w+>/')
def example1pages(name):
    return "<h1>You enter <span class=\"name\" style=\"color: red\">{name}</span> page</h1>".format(name=name)


#
# Routes for example 2
#
@route('/example2/')
@view('example2')
def example2():
    return {}


@route('/example2/saved/')
def example2saved():
    return "<h1>Saved</h1>"


#
# Routes for example 3
#
@route('/example3/')
@view('example3')
def example3():
    user = get_user()
    if user is not None:
        count = len(Message.objects.filter(lambda m: user in m.users_notify))
        msgs = Message.objects.filter(lambda m: user in m.users, owner=user)
        return template('example3logged', dict(user=user, messages=msgs, newsCount=count))
    else:
        return template('example3', {})


@route('/example3/message/create/', method='POST')
def example3post():
    user = get_user()
    if user is not None:
        message = request.POST['message']
        if message:
            Message.objects.create(user, message)
        redirect('/example3/')
    else:
        redirect('/example3/login/')


@route('/example3/message/<type>/<id>/')
def example3get(type, id):
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
        redirect('/example3/')
    else:
        redirect('/example3/login/')


@route('/example3/login/')
@view('example3login')
def example3login():
    if get_user():
        redirect('/example3/')
    return dict(username='', error=False)


@route('/example3/login/', method='POST')
@view('example3login')
def example3login():
    username = request.POST['username']
    password = request.POST['password']
    error = False
    user = authenticate(username, password)
    if user:
        login(user)
        redirect('/example3/')
    else:
        error = True
    return dict(username=username, error=error)


@route('/example3/logout/')
def example3logout():
    session = request.get_cookie(SESSION_NAME)
    if session:
        user = User.objects.find(session=session)
        if user:
            logout(user)
    redirect('/example3/')


@route('/example3/signup/')
@view('example3signup')
def example3signup():
    if get_user():
        redirect('/example3/')
    return dict(email='', username='', errors=[])


@route('/example3/signup/', method='POST')
@view('example3signup')
def example3signup():
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    errors = []
    if not email or not re.match(r'^\w{3,12}@\w{2,8}\.\w{2,3}$', email):
        errors.append('Invalid email')
    if not username or not re.match(r'^\w{3,8}$', username):
        errors.append('Username - 3 latin characters or number')
    if not password or len(password) < 8:
        errors.append('Password - 8 characters')
    if User.objects.find(name=username):
        errors.append('Such user already registered')
    if not errors:
        User.objects.create(email, username, password)
        redirect("/example3/login/")
    return dict(email=email, username=username, errors=errors)


@route('/example3/db/<type>/')
def example3db(type):
    if type == 'dump':
        User.objects.dump()
        Message.objects.dump()
    elif type == 'load':
        User.objects.load()
        Message.objects.load()
    elif type == 'clear':
        User.objects.clear()
        Message.objects.clear()
    elif type == 'test':
        # Stub! Add some test data to models
        user_test = User('', 'Test', 'pass')
        user_test2 = User('', 'Test2', 'pass')
        User.objects.add(user_test)
        User.objects.add(user_test2)
        Message.objects.create(user_test, "Some message #tag #new")
        Message.objects.create(user_test2, "One more message #post @Test")
    else:
        abort(404, 'No such command "dump|load|clear"')