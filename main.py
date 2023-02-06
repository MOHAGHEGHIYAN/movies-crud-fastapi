from fastapi import FastAPI
from mysql import connector

import os

app = FastAPI()


db = connector.connect(
    host=os.getenv("MYSQL_DB_HOST"),
    port=os.getenv("MYSQL_DB_PORT"),
    user=os.getenv("MYSQL_DB_USER"),
    password=os.getenv("MYSQL_DB_PASS"),
    database=os.getenv("MYSQL_DB_NAME"),
)
db_cursor = db.cursor()


@app.get("/")
async def root():
    return {"message": "hello, world!"}


@app.get("/movies/")
def get_movies():
    db_cursor.execute("SELECT * FROM movies")
    return db_cursor.fetchall()


@app.get("/movies/{movie_id}/")
def get_movie(movie_id: int):
    sql = "SELECT * FROM movies WHERE id=%s"
    values = (movie_id,)
    db_cursor.execute(sql, values)
    if movies := db_cursor.fetchall():
        return movies[0]
    else:
        return movie_not_found_response(movie_id)


def movie_not_found_response(movie_id):
    return {"error": f" no movie found for id {movie_id}"}


@app.post("/movies/")
def create_movie(movie: dict):
    sql = "INSERT INTO movies (title, genres) VALUES (%s, %s)"
    val = (movie["title"], movie["genres"])
    db_cursor.execute(sql, val)
    db.commit()
    return {"message": "new movie created"}


@app.patch("/movies/{movie_id}")
def update_movie(movie_id: int, movie: dict):
    sql = "UPDATE movies SET title=%s, genres=%s WHERE id=%s"
    val = (movie["title"], movie["genres"], movie_id)
    db_cursor.execute(sql, val)
    db.commit()
    return {"message": "movie updated"}


@app.delete("/movies/{movie_id}/")
def delete_movie(movie_id: int):
    sql = "DELETE FROM movies WHERE id=%s"
    val = (movie_id,)
    db_cursor.execute(sql, val)
    db.commit()
    return {"message": "movie deleted"}
