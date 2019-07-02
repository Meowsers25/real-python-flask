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

if __name__ == "__main__":
    # use run method to run app locally
    app.run()




