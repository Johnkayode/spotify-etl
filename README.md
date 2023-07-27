# etl-pipeline
ETL Pipeline to obtain tracks and their information from a user's recently played tracks on Spotify.

- Spotify API
- Airflow
- AWS S3



# SETUP
## Spotify API Access

- Ensure you have a Spotify account created
- Register Your Application
    - Go to the [**Dashboard**](https://developer.spotify.com/dashboard/applications) page on the Spotify Developer site
    - Click on **CR an APP**. Provide your app name and app description and then click create.
    - Click on **SETTINGS** then **EDIT** and provide a redirect URI (You can get a redirect url from [webhook.site](https://webhook.site) and then click save.
    - Copy and save your Client ID and Client Secret
- Create an `.env` file using the `.env.example` format and fill the variables
- Run `python -m spotify.auth.authorize` and copy the authorization url to your browser
- Check the `REDIRECT_URI` set, check the query string of the request sent for `code`)
