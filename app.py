from flask import Flask, request
import operations

app = Flask(__name__)

@app.get("/add")
def math_add():
    """this function accepts two params and return the sum"""
    term_a = request.args.get('a')
    term_b = request.args.get('b')
    return f"""{operations.add(int(term_a),int(term_b))}"""

@app.get('/sub')
def math_sub():
    """this function accepts two params and return the subtraction of two params"""

    term_a = request.args.get('a')
    term_b = request.args.get('b')
    return f"""{operations.sub(int(term_a), int(term_b))}"""

@app.get('/mult')
def math_mult():
    """this function accepts two params and return the product of two params"""

    term_a = request.args.get('a')
    term_b = request.args.get('b')
    return f"""{operations.mult(int(term_a), int(term_b))}"""

@app.get('/div')
def math_div():
    """this function accepts two params and return the division of two params"""

    term_a = request.args.get('a')
    term_b = request.args.get('b')
    return f"""{operations.div(int(term_a), int(term_b))}"""