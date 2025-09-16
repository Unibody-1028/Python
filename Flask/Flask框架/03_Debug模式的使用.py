from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    c=1/0
    return 'Hello'

if __name__=='__main__':
    #app.run(debug=True)
    app.debug = True
    app.run()
