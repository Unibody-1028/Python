from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index22.html',param1=1.1)

if __name__ == '__main__':
    app.run(debug=True,port=8088)


