# Spotify Personal Data Exporter

This is a CLI to help export personal data from your Spotify account to files. Currently, it only supports exporting 
your "Liked Songs" playlist to a `.csv` file.

Other online tools already exist to export data from public playlists etc.

## Setup (needs to be done once)

1. Go to https://developer.spotify.com & sign in with your Spotify account
2. Go to the dashboard & click "Create app"
3. Pick any name and description, and for Redirect URIs add the following URI: `http://127.0.0.1/callback`
4. Check the `Web API` option & create the application
5. Save the Client ID & client secret in a secure place

## Usage

Run `python -m app.main --help` for more info

For any questions feel free to reach out at `deansg@gmail.com`
