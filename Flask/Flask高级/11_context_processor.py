from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print('22222222222')
    return render_template('11_index.html')

@app.route('/home/')
def home():
    print('3333333333')
    return render_template('11_home.html')


@app.context_processor
def context_process():
    print('11111111')
    return {'uname':'bob'}




if __name__ == '__main__':
    app.run(debug=True,port=8088)



