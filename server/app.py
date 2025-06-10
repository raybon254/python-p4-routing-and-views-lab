#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<name>')
def print_string(name):
    print (name)
    return name

@app.route('/count/<int:num>')
def count(num):
    result = ''
    for i in range(num):
        result += f"{i}\n"
    return result

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    num1 = int(num1)
    num2 = int(num2)
    if operation == "+":
        res = num1 + num2
    if operation == "-":
        res = num1 - num2
    if operation == "div":
        res = num1 / num2
    if operation == "*":
        res = num1 * num2
    if operation == "%":
        res = num1 % num2
    return str(res)




if __name__ == '__main__':
    app.run(port=5555, debug=True)
