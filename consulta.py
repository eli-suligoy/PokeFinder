import requests
import json

while True:
    pokemon=input("Ingrese numero de pokemon: ")
    pagina="https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon)

    datos=requests.get(url=pagina)

    datos=datos.json()

    print(datos.keys())