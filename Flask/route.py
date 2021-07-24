from flask import Flask,render_template,make_response 
from middleware import chatboy
import os 

def init_apiroutes(app):
    if app:
        app.add_url_rule('/chatbot', 'chatboy', chatboy, methods=['GET'])
        
         
def init_pageroutes(app):
    if app:
        app.add_url_rule('/', 'page_chatbot', page_chatbot , methods = ['GET', 'POST']) 
        
        
def page_chatbot():
    # path = os.getcwd()
    # print(os.path.join(path, 'data', 'intents.json'))
    return render_template('index.html')