import json
import psycopg2
from flask import Flask, Response


from utils import retrieve_most_played_track, retrieve_top_played_artists



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
    sql = retrieve_most_played_track()
    cursor.execute(sql)
    result = cursor.fetchall()
    _most_played_track = result[0] if result else None

    sql = retrieve_top_played_artists()
    cursor.execute(sql)
    result = cursor.fetchall()
    _top_played_artists = result if result else None
    

    conn.close()

    most_played_track = {
        "name": _most_played_track[0],
        "artist": _most_played_track[1],
        "album_art_url": _most_played_track[2],
        "play_count": _most_played_track[3],
    }

    top_played_artists = list()

    for artist in _top_played_artists:
        top_played_artists.append(
            {
                "name": artist[0],
                "genres": artist[1],
                "play_count": artist[2]
            }
        )

    data = {
        "all_tracks": _all_tracks_count,
        "most_played_track": most_played_track,
        "top_played_artists": top_played_artists
    }

    return Response(status=200, response=json.dumps(data))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)