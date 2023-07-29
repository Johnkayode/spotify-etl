import base64
import requests
from decouple import config


CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
ACCESS_TOKEN = config('ACCESS_TOKEN')
REFRESH_TOKEN  = config("REFRESH_TOKEN")
REDIRECT_URI = config("REDIRECT_URI")



def get_access_token() -> str:
    # TODO: refresh access token if access token has expired
    try:
       return refresh_access_token()

    except:
        return ACCESS_TOKEN


def refresh_access_token(
        refresh_token: str = REFRESH_TOKEN, 
        client_id: str = CLIENT_ID,
        client_secret: str = CLIENT_SECRET
    ) -> str:

    url = "https://accounts.spotify.com/api/token"
    credentials = "%s:%s" % (client_id, client_secret)
    base64_encoded = base64.b64encode(credentials.encode()).decode()
    response = requests.post(
        url,
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
        headers={"Authorization": "Basic " + base64_encoded},
    )

    response_json = response.json()
    return response_json.get("access_token")


def get_token_from_authorization_code(
    authorization_code: str,
    client_id: str = CLIENT_ID,
    client_secret: str = CLIENT_SECRET,
    redirect_uri: str = REDIRECT_URI
    ) -> str:

    url = "https://accounts.spotify.com/api/token"
    credentials = "%s:%s" % (client_id, client_secret)
    base64_encoded = base64.b64encode(credentials.encode()).decode()
    response = requests.post(
        url,
        data={"grant_type": "authorization_code", "code": authorization_code, "redirect_uri": redirect_uri},
        headers={"Authorization": "Basic " + base64_encoded},
    )

    response_json = response.json()
    _access_token = response_json.get("access_token")
    _refresh_token = response_json.get("refresh_token")

    return _access_token, _refresh_token