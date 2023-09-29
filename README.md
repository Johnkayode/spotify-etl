# spotify-etl
ETL pipeline to retrieve tracks and their information from a user's recently played tracks on Spotify.

- Spotify API
- iwAirflow
- PostgreSQL
- Docker

# Setup

## Spotify API Access

- Ensure you have a Spotify account created
- Register Your Application
    - Go to the [**Dashboard**](https://developer.spotify.com/dashboard/) page on the Spotify Developer site
    - Click on **Create App**. Provide your app name and app description and then click create.
    - Click on **Settings** then **EDIT** and provide a redirect URI (You can get a redirect url from [webhook.site](https://webhook.site)) and then click save.
    - Copy and save your Client ID and Client Secret
- Create an `.env` file using the `.env.example` format and fill the variables
- Run `python -m spotify.auth.authorize` and copy the authorization url to your browser
- Visit the `REDIRECT_URI` set in the step above, check the query paramaters of the request sent for `code`, the **authorization_code**)
- Run `python -m spotify.auth.token -c your_authorization_code` or `python -m spotify.auth.token --code your_authorization_code` to get your **access** and **refresh** tokens.
- Set the tokens in yout `.env` file.

## Run Project

- Run `docker run --build` to build and run the containers
- Open `localhost:8080` to view the Airflow UI (You might need to create a user)
- Run the DAG
- Open `localhost:5000` to view the API
