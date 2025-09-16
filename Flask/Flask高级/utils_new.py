from flask import g

def func_a():
    return f'func_a uname:{g.uname}'
def func_b():
    return f'func_b uname:{g.uname}'
def func_c():
    return f'func_c uname:{g.uname}'

