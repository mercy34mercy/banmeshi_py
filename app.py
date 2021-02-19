# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world'

@app.route('/hello')
def indexs():
    return 'hello'
@app.route('/hello')
def indexs():
    return 'hello'



if __name__ == '__main__':
    app.run()
