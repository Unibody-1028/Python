from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    items = ['python','c','c++','java','golang']
    person = {'uname':'Jack','age':22,'gender':'male'}
    return render_template('index30.html',items = items,person = person)

if __name__ == '__main__':
    app.run(debug=True,port=8088)