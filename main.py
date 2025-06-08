import csv

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"


# Rename to spotify personal data exporter
def run():
    with open("results.csv", "w", encoding="utf-8", newline='') as f:
        # noinspection PyTypeChecker
        writer = csv.DictWriter(f, fieldnames=[
            "#", "Title", "Artist names", "Album", "Date added", "ISRC", "URL", "Is playable"
        ])
        _run(writer)


def _run(writer: csv.DictWriter):
    writer.writeheader()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    offset = 0
    while True:
        results = sp.current_user_saved_tracks(limit=50, offset=offset)
        items = results['items']
        if not items:
            return
        for idx, item in enumerate(items):
            added_at = item['added_at']
            track = item['track']
            is_local: bool = track['is_local']
            if is_local:
                print("Skipping local track")
                continue
            name = track['name']
            artist_names = ', '.join(artist['name'] for artist in track['artists'])
            isrc = track['external_ids']['isrc']
            url = track['external_urls']['spotify']
            is_playable = track['is_playable']
            album_name = track["album"]["name"]
            writer.writerow({
                "#": offset + idx + 1,
                "Title": name,
                "Artist names": artist_names,
                "Album": album_name,
                "Date added": added_at,
                "ISRC": isrc,
                "URL": url,
                "Is playable": is_playable,
            })
        offset += len(items)
        print(f"\rProcessed {offset} results", end="")



if __name__ == '__main__':
    run()
