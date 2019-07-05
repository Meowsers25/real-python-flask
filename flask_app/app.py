#  imports the Flask class from flask library
from flask import Flask 
  
#  Instance of Flask class created, and assigned variable name app
app = Flask(__name__)

# decorators to define 2 routes
@app.route('/')
@app.route('/hello')

# function returns string "Hello World"
def hello_world():
    return "Hello, World!"

# @app.route('/test')
# def search():
#     return "Hello, Luna"

@app.route('/test/<search_query>')
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "Correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "Correct float"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "URL Path"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "chris":
        return f"Hello, {name}", 200
    else: 
        return "Not found", 404
    
if __name__ == "__main__":
    # use run method to run app locally
    app.run()




