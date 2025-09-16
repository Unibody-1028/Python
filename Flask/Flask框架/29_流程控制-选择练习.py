from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index29.html')

@app.route('/login2/')
def login():
    user = request.args.get('user')
    return render_template('index29.html',user=user)

if __name__ == '__main__':
    app.run(debug=True,port=8088)

