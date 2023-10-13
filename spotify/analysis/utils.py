
def retrieve_top_played_tracks():
    sql = """
    SELECT track.name, artist.name, track.album_art_link, COUNT(*) as play_count
    FROM RecentlyPlayedTracks track
    JOIN Artists artist ON track.artist_id = artist.artist_id
    GROUP BY track.name, artist.name, track.album_art_link
    ORDER BY play_count DESC
    LIMIT 5;
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

def retrieve_top_played_genres():
    sql = """
    SELECT genre, COUNT(*) as genre_count
    FROM (
        SELECT DISTINCT ON (track.track_id) track.track_id, unnest(artist.genres) as genre
        FROM RecentlyPlayedTracks track
        JOIN Artists artist ON track.artist_id = artist.artist_id
    ) AS subquery
    GROUP BY genre
    ORDER BY genre_count DESC
    LIMIT 10;
    """
    return sql



