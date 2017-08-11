# !usr/bin/env python3
# -*- coding: utf-8 -*-
# my first web program

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/usr/<name>')
def index(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()
