from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
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
    return JSONResponse(content=jsonable_encoder(movies), status_code=status.HTTP_200_OK)


@movies.get('/{id}', response_model=Movie)
def get_movie(id: Id):
    movie: Movie | None = db.get_movie(id)
    if not (movie):
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(movie), status_code=status.HTTP_200_OK)


@movies.post('/', response_model=Movie)
def create_movie(movie: MovieCreate):
    new_movie: Movie | None = db.create_movie(
        title=movie.title,
        release=movie.release,
        rated=movie.rated,
        image=movie.image,
    )
    return JSONResponse(content=jsonable_encoder(new_movie), status_code=status.HTTP_201_CREATED)


@movies.put('/{id}', response_model=Movie)
def update_movie(movie: MoviePut, id: Id):
    updated_movie: Movie | None = db.update_movie(movie, id)
    if not (updated_movie):
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(updated_movie), status_code=status.HTTP_200_OK)
