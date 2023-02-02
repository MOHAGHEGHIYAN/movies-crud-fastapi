from fastapi import FastAPI


app = FastAPI()


movies = [
    {"id": 1, "title": "The Shawshank Redemption", "genres": ["Crime", "Drama"]},
    {"id": 2, "title": "The Godfather", "genres": ["Crime", "Drama"]},
]


@app.get("/")
async def root():
    return {"message": "hello, world!"}


@app.get("/movies")
def get_movies():
    return movies
