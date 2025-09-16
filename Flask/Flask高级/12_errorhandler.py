from flask import Flask, g, render_template,abort

app = Flask(__name__)


@app.route('/')
def index():
    print(g.uname)
    return 'Hello'

@app.errorhandler(500)
def server_error(error):
    return render_template('12_500.html'),500

@app.errorhandler(404)
def server_error(error):
    return render_template('12_404.html'),404

@app.route('/home/')
def home():
    return abort(500)

if __name__ == '__main__':
    app.run(debug=False,port=8088)

