# spotify-etl
ETL pipeline to retrieve tracks and their information from a user's recently played tracks on Spotify.

- Spotify API
- Airflow
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
- Create Airflow user 
`docker exec -it airflow-webserver airflow users create 
          --username admin 
          --firstname FIRST_NAME 
          --lastname LAST_NAME 
          --role Admin 
          --email admin@example.org`
- Open `localhost:8080` to view the Airflow UI (You need to create an admin user)
- Create a default connection for Postgres (conn_id: postgres_default)
- Run the DAG
- Open `localhost:5000` to view the API
