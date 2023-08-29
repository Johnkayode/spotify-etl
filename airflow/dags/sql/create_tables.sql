CREATE TABLE IF NOT EXISTS Artists (
    artist_id SERIAL PRIMARY KEY,
    spotify_id  VARCHAR(255) NOT NULL UNIQUE,
    name  VARCHAR(255) NOT NULL,
    genres  TEXT[]
);

CREATE TABLE IF NOT EXISTS RecentlyPlayedTracks (
    play_id SERIAL PRIMARY KEY,
    track_id VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    artist_id INT NOT NULL,
    album_id VARCHAR(255),
    album_name VARCHAR(255),
    album_art_link VARCHAR(255),
    duration VARCHAR(255),  
    explicit BOOLEAN,
    popularity INT,    
    played_at TIMESTAMP,  

    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id),
    CONSTRAINT unique_track_play UNIQUE (track_id, played_at)
);






