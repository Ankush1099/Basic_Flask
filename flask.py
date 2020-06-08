# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 00:29:02 2020

@author: Ankush
"""


from flask import Flask
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    return "All Books in {} category".format(genre)

if __name__ == "__main__":
    app.run()