from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index21.html')

@app.route('/home2/')
def home():
    return 'home'
@app.route('/home1/<int:id>')
def home1(id):
    return 'home'

if __name__ == '__main__':
    app.run(debug=True,port=8088)


