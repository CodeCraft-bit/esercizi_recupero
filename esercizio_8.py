class Movie:
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = True) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self) -> None:
        if self.is_rented:
            print(f"Il {self.title} è già noleggiato")
        else:
            self.is_rented = True
        
    def return_movie(self) -> None:
        if not self.is_rented:
            print (f"Il film non è stato noleggiato a nessuno")
        else:
            self.is_rented = False
        
class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:
        if movie.is_rented:
            print(f"Il film {movie.title} è già noleggiato")
        else:
            movie.rent()
            self.rented_movies.append(movie)
            
    def return_movie(self, movie: Movie) -> None:
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente")

class VideoRentalstore:
    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}) -> None:
        self.movies = movies
        self.customers = customers   
    
    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        if movie_id not in self.movies:
            # oppure movie: Movie = Movie(movie-id, title, director)
            #self.movie[movie_id] = movie
            self.movies.update((movie_id, Movie(movie_id, title, director)))
        else:
            print(f"Il film con ID {movie_id} esiste già")
        
    def register_customers(self, customer_id: str, name: str) -> None:
        if customer_id not in self.customers:
            self.customers.update((customer_id, Customer(customer_id, name, rented_movies=list[Movie])))
        else:
            print(f"Il cliente con ID {customer_id} è già registrato")
        
    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        if movie_id in self.movies and customer_id in self.customers:
            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].rent_movie(movie)
        else:
            print("Cliente o film non trovato")

    def return_movie(self, customer_id: str, movie_id: str) -> None:
        if movie_id in self.movies and customer_id in self.customers:
            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].return_movie(movie)
        else:
            print("Cliente o film non trovato")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            print("Il cliente non esiste")

    def get_all_movies(self) -> list[Movie]:
        film_noleggiati: list[Movie] = []
        for customer_id, customer in self.customers.items():
            film_noleggiati += customer.rented_movies
        return film_noleggiati

        
        
        