from flask import Flask
from middleware import chatboy
from route import init_apiroutes,init_pageroutes




#app = Flask(__name__, static_url_path="/static", static_folder=r'C:\Users\anike\Downloads\personal_work\Chatbot\Flask_chatbot\static')   
app = Flask(__name__)   

init_apiroutes(app)
init_pageroutes(app)

if __name__ == '__main__':
    app.run(debug=True)
