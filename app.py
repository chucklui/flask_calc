# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.get("/add")
def math_add():
    """this function accepts two params and return the sum"""
    term_a = request.args.get('<int:a>')
    term_b = request.args.get('<int:b>')
    return f"""{operations.add(term_a,term_b)}"""

@app.get('/sub')
def math_sub():
    """this function accepts two params and return the subtraction of two params"""

    term_a = request.args.get('<int:a>')
    term_b = request.args.get('<int:b>')
    return f"""{operations.add(term_a,term_b)}"""

@app.get('/mult')
def math_mult():
    """this function accepts two params and return the product of two params"""

    term_a = request.args.get('<int:a>')
    term_b = request.args.get('<int:b>')
    return f"""{operations.add(term_a,term_b)}"""

@app.get('/div')
def math_div():
    """this function accepts two params and return the division of two params"""

    term_a = request.args.get('<int:a>')
    term_b = request.args.get('<int:b>')
    return f"""{operations.add(term_a,term_b)}"""