from ApiVehicles import cargar_api
from ApiStarships import cargar_api
from ApiSpecies import cargar_api
from ApiPlanets import cargar_api
from ApiPeople import cargar_api
from ApiFilms import cargar_api
from Film import Film

class App:
    film_obj=[]


    def crear_films(self):
        dbfilms=cargar_api("https://www.swapi.tech/api/films/")
        for film in dbfilms:
            self.film_obj.append(Film(film["title"]),(film["episode_id"]),(film["release_date"]),(film["opening_crawl"]),(film["director"]) )
        
    def print_films(self):
        for film in self.film_obj:
            print(f"Titulo: {film.title}")
            print(f"Numero de episodio: {film.episode_id}")
            print(f"Fecha de lanzamiento: {film.release_date}")
            print(f"Opening Crawl: {film.opening_crawl}")
            print(f"Director: {film.director}")
            print("---")