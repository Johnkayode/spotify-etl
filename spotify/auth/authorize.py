from decouple import config


CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
REDIRECT_URI  = config("REDIRECT_URI")


def get_authorization_url(client_id: str=CLIENT_ID, redirect_uri: str=REDIRECT_URI):
    scope="user-read-recently-played"
    url = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
    return url


if __name__ == "__main__":
    print(get_authorization_url())




