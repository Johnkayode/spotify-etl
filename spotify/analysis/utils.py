
def retrieve_most_played_track():
    sql = """
    SELECT track.name, artist.name, track.album_art_link, COUNT(*) as play_count
    FROM RecentlyPlayedTracks track
    JOIN Artists artist ON track.artist_id = artist.artist_id
    GROUP BY track.name, artist.name, track.album_art_link
    ORDER BY play_count DESC
    LIMIT 1;
    """
    return sql

def retrieve_top_played_artists():
    sql = """
    SELECT artist.name, artist.genres, COUNT(*) as play_count
    FROM RecentlyPlayedTracks track
    JOIN Artists artist ON track.artist_id = artist.artist_id
    GROUP BY artist.name, artist.genres
    ORDER BY play_count DESC
    LIMIT 5;
    """
    return sql


