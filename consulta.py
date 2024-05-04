import requests

def consultar(dato):
    pagina="https://pokeapi.co/api/v2/pokemon/{}/".format(dato)
    datos=requests.get(url=pagina)
    datos=datos.json()
    nombre=datos["name"]
    foto=datos["sprites"]["front_default"]
    resultado={"nombre":nombre,"foto":foto}
    return resultado

if __name__== '__main__':
    while True:
        pokemon=input("Ingrese numero de pokemon: ")
        consultar(pokemon)
