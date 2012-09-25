# -*- coding: utf-8 -*-
from app.bottle import load, run
import conf


load('app.controls')

run(host=conf.SERVER_HOST, port=conf.SERVER_PORT, reloader=True, debug=True)