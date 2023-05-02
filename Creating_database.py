import requests
import sqlite3

sparql_query = """
SELECT ?movie ?imdbId WHERE {
  ?movie wdt:P31 wd:Q11424;  # Instance of film
        wdt:P577 ?releaseDate;  # Release date
        wdt:P345 ?imdbId.  # IMDb ID
  FILTER (YEAR(?releaseDate) > 2013).
}
"""

api_url = 'https://query.wikidata.org/sparql'
response = requests.get(
    api_url, params={'query': sparql_query, 'format': 'json'})


if response.status_code == 200:
    data = response.json()
    movies = data['results']['bindings']
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id TEXT,
            imdb_id TEXT
        )
    """)

    for movie in movies:
        movie_id = movie['movie']['value']
        imdb_id = movie['imdbId']['value']

        cursor.execute("""
            INSERT OR REPLACE INTO movies (movie_id, imdb_id)
            VALUES (?, ?)
        """, (movie_id, imdb_id))

        print(f"Movie ID: {movie_id}, IMDb ID: {imdb_id}")

    conn.commit()
    conn.close()
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT movie_id, imdb_id FROM movies")
    rows = cursor.fetchall()

    for row in rows:
        movie_id, imdb_id = row
        print(f"Movie ID: {movie_id}, IMDb ID: {imdb_id}")
    conn.close()
else:
    print("Request failed with status code:", response.status_code)
