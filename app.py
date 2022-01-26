from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add")
# @app.get("/math/add")
def math_add():
    """this function accepts two params and return the sum"""

    term_a = request.args.get('a')
    term_b = request.args.get('b')
    return str(add(int(term_a),int(term_b)))

@app.get('/sub')
# @app.get('/math/sub')
def math_sub():
    """this function accepts two params and return the subtraction of two params"""

    term_a = request.args.get('a')
    term_b = request.args.get('b')
    return str(sub(int(term_a), int(term_b)))

@app.get('/mult')
# @app.get('/math/mult')
def math_mult():
    """this function accepts two params and return the product of two params"""

    term_a = request.args.get('a')
    term_b = request.args.get('b')
    return str(mult(int(term_a), int(term_b)))

@app.get('/div')
# @app.get('/math/div')
def math_div():
    """this function accepts two params and return the division of two params"""

    term_a = request.args.get('a')
    term_b = request.args.get('b')
    return str(div(int(term_a), int(term_b)))