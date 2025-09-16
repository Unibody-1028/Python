from flask import Flask

app = Flask(__name__)

@app.route('/index/<int:id>')
def index(id):
    return f'<h1>Hello<h1>{id}'

if __name__ == '__main__':
    app.run(debug=True)


