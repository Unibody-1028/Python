from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('index23.html',name='jack')
    #return render_template('index23.html')
    return render_template('index23.html',name=None)

if __name__ == '__main__':
    app.run(debug=True,port=8088)



