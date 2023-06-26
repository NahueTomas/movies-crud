from uuid import uuid4
from models.movie import Id, Title, Release, Rated, Image, Movie
from schemas.movie import MoviePut
from db.example import example_movies

Movies = list[Movie]


class Database:
    movies: Movies = []

    # Filling the list
    def __init__(self):
        for movie in example_movies:
            self.create_movie(
                title=movie.title,
                release=movie.release,
                rated=movie.rated,
                image=movie.image
            )

    def create_movie(self, title: Title, release: Release, rated: Rated = "N/A", image: Image = '') -> Movie:
        id: Id = uuid4()
        new_movie: Movie = Movie(id, title, release, rated, image)

        self.movies.append(new_movie)
        return new_movie

    def get_all_movies(self) -> Movies:
        return self.movies

    def get_movie(self, id: Id) -> Movie | None:
        for item in self.movies:
            if str(item.id) == str(id):
                return item
        return None

    def update_movie(self, data: MoviePut, id) -> Movie | None:
        for item in self.movies:
            if str(item.id) == str(id):
                if (data.title):
                    item.title = data.title
                if (data.release):
                    item.release = data.release
                if (data.rated):
                    item.rated = data.rated
                if (data.image):
                    item.image = data.image
                return item
        return None


db = Database()
