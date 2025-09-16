from flask import Flask,render_template,template_rendered


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/home/')
def home():
    return render_template('16_home.html')

def render_func(sender,template,context):
    print(sender)
    print(template)
    print(context)
template_rendered.connect(render_func)



if __name__ == '__main__':
    app.run(debug=True,port=8088)

