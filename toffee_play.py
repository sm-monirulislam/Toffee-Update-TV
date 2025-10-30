import requests
import json

# ✅ Toffee Auto Playlist Builder Script

def fetch_toffee_channels(api_url, output_file):
    response = requests.get(api_url)
    data = response.json()
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")  # M3U Header
        for item in data["data"]:
            title = item.get("title", "Unknown")
            stream = item.get("stream_url", "")
            f.write(f'#EXTINF:-1 tvg-name="{title}" group-title="Toffee",{title}\n{stream}\n')

if __name__ == "__main__":
    api_url = "https://toffeelive.com/api/web/playback/sy5m-JQBv9knK3AHYTTk"
    fetch_toffee_channels(api_url, "toffee_playlist.m3u")
    print("✅ Playlist generated successfully!")
