

class Artist:
    id: str
    name: str
    genres: list

    def __init__(self, artist: dict) -> None:
        self.id = str(artist["id"])
        self.name = artist["name"]
        self.genres = artist["genres"]

    @property
    def __to_dict__(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "genres": self.genres
        }

    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self) -> str:
        return self.__repr__()