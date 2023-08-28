CREATE TABLE IF NOT EXISTS Artists (
    artist_id INT PRIMARY KEY AUTO_INCREMENT,
    spotify_id  VARCHAR(255) NOT_NULL UNIQUE,
    name  VARCHAR(255) NOT NULL,
    genres  TEXT [],
);


CREATE TABLE IF NOT EXISTS RecentlyPlayedTracks (
    play_id INT PRIMARY KEY AUTO_INCREMENT,
    track_id VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    artist_id INT NOT NULL,
    album_id VARCHAR(255),
    album_name VARCHAR(255),
    album_art_link VARCHAR(255),
    duration VARCHAR(255),
    explicit BOOLEAN, 
    popularity VARCHAR(255),
    played_at DATE,

    FOREIGN KEY (artist_id) REFERENCES Artists(id),
    UNIQUE KEY unique_track_play (track_id, played_at)

);

