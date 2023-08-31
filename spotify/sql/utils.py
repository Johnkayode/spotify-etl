
def get_or_create_artist(artist: dict) -> str:
    sql_template = """
    INSERT INTO Artists (spotify_id, name, genres)
    VALUES ('{id}', '{name}', ARRAY{genres}::TEXT[])
    ON CONFLICT (spotify_id) DO NOTHING;
    
    SELECT artist_id FROM Artists WHERE spotify_id = '{id}';
    """
    sql = sql_template.format(
        id=artist["id"],
        name=artist["name"],
        genres=artist["genres"]
    )
    return sql

def create_track(track: dict, artist_id: int):
    sql_template = """
    INSERT INTO RecentlyPlayedTracks (track_id, name, artist_id, album_id, album_name, album_art_link, duration, explicit, popularity, played_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    values = (
        track.get("id"),
        track.get("name"),
        artist_id,
        track.get("album_id"),
        track.get("album_name"),
        track.get("album_art_link"),
        track.get("duration"),
        "TRUE" if track.get("explicit") else "FALSE",
        track.get("popularity"),
        track.get("played_at")
    )
    return sql_template, values

def retrieve_last_played_at():
    sql = """
    SELECT MAX(played_at) from RecentlyPlayedTracks;
    """
    return sql
