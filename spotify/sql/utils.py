import json

def get_or_create_artist(artist: dict) -> str:
    sql_template = """
    INSERT INTO Artists (spotify_id, name, genres)
    VALUES ('{id}', '{name}', {genres})
    ON CONFLICT (spotify_id) DO NOTHING;
    
    SELECT id FROM Artists WHERE spotify_id = '{id}';
    """
    sql = sql_template.format(
        id=artist["id"],
        name=artist["name"],
        genres=json.dumps(artist["genres"])
    )
    return sql

def create_track(track: dict, artist_id: int):
    sql_template = """
    INSERT INTO RecentlyPlayedTracks (track_id, name, artist_id, album_id, album_name, album_art_link, duration, explicit, popularity, played_at)
    VALUES ('{id}', '{name}', '{artist_id}', '{album_id}', '{album_name}', '{album_art_link}', '{duration}', '{explicit}', '{popularity}', '{played_at}');
    """
    sql = sql_template.format(
        id=track.get("id"),
        name=track.get("name"),
        artist_id=artist_id,
        album_id=track.get("album_id"),
        album_name=track.get("album_name"),
        album_art_link=track.get("album_art_link"),
        duration=track.get("duration"),
        explicit="TRUE" if track.get("explicit") else "FALSE",
        popularity=track.get("popularity"),
        played_at=track.get("played_at")
    )
    return sql


