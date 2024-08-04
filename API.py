import requests as rq

class API:

    def cargar_api(self, link):
        response = rq.get(link)
        print(response.json())
        return response.json()

    def cargar_personajes(self):
        personajes = self.cargar_api('https://www.swapi.tech/api/people')
        return personajes

