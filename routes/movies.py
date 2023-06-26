from fastapi import APIRouter

from db.database import db, Movies
from models.movie import Movie, Id
from schemas.movie import MovieCreate, MoviePut

movies = APIRouter(
    prefix="/movies",
    tags=['Movies'],
)


@movies.get('/')
def get_all() -> Movies:
    movies: Movies = db.get_all_movies()
    return movies


@movies.get('/{id}')
def get_movie(id: Id) -> Movie | None:
    movie: Movie | None = db.get_movie(id)
    return movie


@movies.post('/')
def create_movie(movie: MovieCreate) -> Movie:
    new_movie: Movie | None = db.create_movie(
        title=movie.title,
        release=movie.release,
        rated=movie.rated,
        image=movie.image,
    )
    return new_movie


@movies.put('/{id}')
def update_movie(movie: MoviePut, id: Id) -> Movie | None:
    updated_movie: Movie | None = db.update_movie(movie, id)
    return updated_movie
