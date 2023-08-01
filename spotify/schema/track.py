from datetime import datetime
from typing import Optional, Any


class Track:
    track: dict
    id: str
    name: str
    lead_artist_id: str
    lead_artist_name: str
    duration: str
    album_id: str
    album_name: str
    album_art_link: str
    popularity: int
    explicit: bool
    played_at: Optional[datetime]

    def __init__(self, track: dict) -> None:
        self.track = track["track"]
        self.played_at = datetime.strptime(track["played_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.id = self.track["id"]
        self.name = self.track["name"]
        self.duration = self.track["duration_ms"]
        self.popularity = self.track["popularity"]
        self.explicit = self.track["explicit"]
        self.lead_artist_id = self.track["artists"][0]["id"]
        self.lead_artist_name = self.track["artists"][0]["name"]
        self.album_id = self.track["album"]["id"]
        self.album_name = self.track["album"]["name"]
        self.album_art_link = self.track["album"]["images"][1]["url"]

    @property
    def __to_dict__(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "popularity": self.popularity,
            "explicit": self.explicit,
            "lead_artist_id": self.lead_artist_id,
            "lead_artist_name": self.lead_artist_name,
            "album_id": self.album_id,
            "album_name": self.album_name,
            "album_art_link": self.album_art_link,
            "played_at": self.played_at
        }
        
    def __repr__(self) -> str:
        return f"{self.name} - {self.lead_artist_name}"

    def __str__(self) -> str:
        return self.__repr__()

      
