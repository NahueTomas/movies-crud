from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response

from db.database import db, Movies
from models.movie import Movie, Id
from schemas.movie import MovieCreate, MoviePut

movies = APIRouter(
    prefix="/movies",
    tags=['Movies'],
)


@movies.get('/', response_model=Movies)
def get_all():
    movies: Movies = db.get_all_movies()
    # Movies to dict
    movies_dict = []
    for movie in movies:
        movie_dict = {
            "id": str(movie.id),
            "title": movie.title,
            "release": movie.release,
            "rated": movie.rated,
            "image": movie.image
        }
        movies_dict.append(movie_dict)
    return JSONResponse(content=movies_dict, status_code=status.HTTP_200_OK)


@movies.get('/{id}', response_model=Movie)
def get_movie(id: Id):
    movie: Movie | None = db.get_movie(id)
    if not (movie):
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    movie_dict = {
        "id": str(movie.id),
        "title": movie.title,
        "release": movie.release,
        "rated": movie.rated,
        "image": movie.image
    }
    return JSONResponse(content=movie_dict, status_code=status.HTTP_200_OK)


@movies.post('/', response_model=Movie)
def create_movie(movie: MovieCreate):
    new_movie: Movie | None = db.create_movie(
        title=movie.title,
        release=movie.release,
        rated=movie.rated,
        image=movie.image,
    )

    movie_dict = {
        "id": str(new_movie.id),
        "title": new_movie.title,
        "release": new_movie.release,
        "rated": new_movie.rated,
        "image": new_movie.image
    }
    return JSONResponse(content=movie_dict, status_code=status.HTTP_201_CREATED)


@movies.put('/{id}', response_model=Movie)
def update_movie(movie: MoviePut, id: Id):
    updated_movie: Movie | None = db.update_movie(movie, id)
    if not (updated_movie):
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    movie_dict = {
        "id": str(updated_movie.id),
        "title": updated_movie.title,
        "release": updated_movie.release,
        "rated": updated_movie.rated,
        "image": updated_movie.image
    }
    return JSONResponse(content=movie_dict, status_code=status.HTTP_200_OK)
