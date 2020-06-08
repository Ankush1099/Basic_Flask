# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:23:16 2020

@author: Ankush
"""

from flask import Flask
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    print(i)
    return 'Hello World'

@app.route('/career/')
def career():
    return 'Career Page'

@app.route('/contact/')
@app.route('/feedback/')
def feedback():
    return 'Feedback Page'

@app.route('/user/<id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)

if __name__ == "__main__":
    app.run()