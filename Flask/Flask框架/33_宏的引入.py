from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    uname = 'jack'

    return render_template('index33.html',uname=uname)

if __name__ == '__main__':
    app.run(debug=True,port=8088)

