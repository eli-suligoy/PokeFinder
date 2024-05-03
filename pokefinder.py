import os
from flask import Flask
from flask import render_template,request,redirect
from flask import send_from_directory

app= Flask(__name__,template_folder='templates')


@app.route("/css/<archivocss>")
def css_link(archivocss):
    return send_from_directory(os.path.join('templates/css/'),archivocss)


@app.route('/')
def index():
    return render_template('/index.html')


if __name__== '__main__':
    app.run(debug=True)