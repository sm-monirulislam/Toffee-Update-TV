import os
import requests

# ✅ Toffee Auto Playlist Builder with Secret Token

def fetch_toffee_channels(api_url, output_file, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_url, headers=headers)
    data = response.json()
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for item in data.get("data", []):
            title = item.get("title", "Unknown Channel")
            stream = item.get("stream_url", "")
            f.write(f'#EXTINF:-1 tvg-name="{title}" group-title="Toffee",{title}\n{stream}\n')

if __name__ == "__main__":
    api_url = "https://toffeelive.com/api/web/playback/sy5m-JQBv9knK3AHYTTk"
    token = os.getenv("TOFFEE_API_TOKEN")
    fetch_toffee_channels(api_url, "toffee_playlist.m3u", token)
    print("✅ Playlist generated successfully with secret token!")
