from API import API

class App:

    def start(self):
        api = API()
        api.cargar_personajes()
        
        print("Starting the app...")