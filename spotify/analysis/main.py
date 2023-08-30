import json
from flask import Flask, Response
from airflow.providers.postgres.hooks.postgres import PostgresHook

from spotify.sql.utils import retrieve_most_played_track, retrieve_top_artists


app = Flask(__name__)

@app.route('/')
def index():
   
    pg_hook = PostgresHook()

    # Fetch the most played track from the database
    sql = retrieve_most_played_track()
    result = pg_hook.get_records(sql)
    _most_played_track = result[0] if result else None

    _top_played_artists = retrieve_top_artists()
    sql = retrieve_most_played_track()
    result = pg_hook.get_records(sql)

    most_played_track = {
        "name": _most_played_track[0],
        "artist": _most_played_track[1],
        "album_art_url": _most_played_track[2],
        "play_count": _most_played_track[3],
    }
    data = {
        "most_played_track": most_played_track,
        "top_played_artists": _top_played_artists
    }

    return Response(status=200, response=json.dumps(data))



if __name__ == '__main__':
    app.run(debug=True)