from fastapi import FastAPI
from routes.movies import movies

app = FastAPI(
    title='Movies',
    description='Movie CRUD API'
)

app.include_router(movies)
