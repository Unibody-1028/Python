from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    info = '<script>alert("Hello")</script>'
    return render_template('index24.html',info=info)

if __name__ == '__main__':
    app.run(debug=True,port=8088)





