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
    try:
        return list(filter(lambda x: x["id"] == movie_id, movies))[0]
    except IndexError:
        return movie_not_found_response(movie_id)


@app.delete("/movies/{movie_id}/")
def delete_movie(movie_id: int):
    index = find_movie_index(movie_id)

    if index <= -1:
        return movie_not_found_response(movie_id)

    del movies[index]
    return {"message": f"movie with id {movie_id} deleted."}


def movie_not_found_response(movie_id):
    return {"error": f" no movie found for id {movie_id}"}


def find_movie_index(movie_id):
    index = -1
    for i, item in enumerate(movies):
        print(i, item)
        if item["id"] == movie_id:
            index = i
            break
    return index


@app.post("/movies/")
def create_movie(movie: dict):
    movies.append(movie)


@app.patch("/movies/{movie_id}")
def update_movie(movie_id: int, movie: dict):
    index = find_movie_index(movie_id)
    if index <= -1:
        return movie_not_found_response(movie_id)

    movies[index].update(movie)
