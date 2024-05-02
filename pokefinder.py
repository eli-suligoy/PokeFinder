from flask import Flask
from flask import render_template,request,redirect

app= Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('/index.html')


if __name__== '__main__':
    app.run(debug=True)