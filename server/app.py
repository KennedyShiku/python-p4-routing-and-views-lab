#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    count = ''
    for i in range(int(parameter)):
        count += str(i) + '\n'
    return count

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_operation(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return "Invalid operation or division by zero", 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
