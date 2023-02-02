from fastapi import FastAPI


app = FastAPI()


movies = [
    {"id": 1, "title": "The Shawshank Redemption", "genres": ["Crime", "Drama"]},
    {"id": 2, "title": "The Godfather", "genres": ["Crime", "Drama"]},
]


@app.get("/")
async def root():
    return {"message": "hello, world!"}


@app.get("/movies/")
def get_movies():
    return movies


@app.get("/movies/{movie_id}/")
def get_movie(movie_id: int):
    movie = None
    try:
        movie = list(filter(lambda x: x["id"] == movie_id, movies))[0]
    except IndexError:
        movie = {"error": f" no movie found for id {movie_id}"}
    return movie


@app.delete("/movies/{movie_id}/")
def delete_movie(movie_id: int):
    index = -1
    for i, item in enumerate(movies):
        print(i, item)
        if item["id"] == movie_id:
            index = i
            break

    response = {}
    if index <= -1:
        return {"error": f" no movie found for id {movie_id}"}

    del movies[index]
    return {"message": f"movie with id {movie_id} deleted."}
