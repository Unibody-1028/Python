from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    uname = 'jack'
    uname1 = 'bob'
    return render_template('index28.html',uname=uname,uname1=uname1)

if __name__ == '__main__':
    app.run(debug=True,port=8088)


