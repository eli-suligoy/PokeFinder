import os
from flask import Flask
from flask import render_template,request,redirect
from flask import send_from_directory
from consulta import consultar

app= Flask(__name__,template_folder='templates')


@app.route("/css/<archivocss>")
def css_link(archivocss):
    return send_from_directory(os.path.join('templates/css/'),archivocss)


@app.route('/', methods=['POST','GET'])
def index():
    nombre=''
    foto='static/pokedex.png'
    try:
        if request.method == 'POST':
            pokemon = request.form.get('pokenum')
            datos=consultar(pokemon)
            nombre=datos['nombre']
            foto=datos['foto']
            print(datos['nombre'])
    except:
        nombre=f"No exite pokemon con ese codigo"      
    return render_template('/index.html', resultado=nombre.title( ), imagen=foto)


if __name__== '__main__':
    app.run(debug=True)