import json
import psycopg2
from flask import Flask, Response


from utils import retrieve_top_played_tracks, retrieve_top_played_artists, retrieve_top_played_genres



app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        host='postgres',  # Use the service name from Docker Compose
        user='airflow',
        password='airflow',
        dbname='airflow'
    )
    cursor = conn.cursor()

    sql = "SELECT COUNT(*) FROM RecentlyPlayedTracks;"
    cursor.execute(sql)
    result = cursor.fetchall()
    _all_tracks_count = result[0][0] if result and result[0] else 0

    # Fetch the most played track from the database
    sql = retrieve_top_played_tracks()
    cursor.execute(sql)
    result = cursor.fetchall()
    _top_played_tracks = result if result else []

    sql = retrieve_top_played_artists()
    cursor.execute(sql)
    result = cursor.fetchall()
    _top_played_artists = result if result else []

    sql = retrieve_top_played_genres()
    cursor.execute(sql)
    result = cursor.fetchall()
    _top_played_genres = result if result else []
    

    conn.close()

    top_played_tracks = list()
    top_played_artists = list()
    top_played_genres = list()

    for track in _top_played_tracks:
        top_played_tracks.append(
            {
                "name": track[0],
                "artist": track[1],
                "album_art_url": track[2],
                "play_count": track[3],
            }
        )

    for artist in _top_played_artists:
        top_played_artists.append(
            {
                "name": artist[0],
                "genres": artist[1],
                "play_count": artist[2]
            }
        )

    for genre in _top_played_genres:
        top_played_genres.append(
            {
                "name": genre[0],
                "play_count": genre[1],
            }
        )

    data = {
        "all_tracks": _all_tracks_count,
        "top_played_tracks": top_played_tracks,
        "top_played_artists": top_played_artists,
        "top_played_genres": top_played_genres
    }

    return Response(status=200, response=json.dumps(data))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)