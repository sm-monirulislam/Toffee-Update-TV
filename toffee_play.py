import os
import requests

def fetch_toffee_channels(api_url, output_file, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_url, headers=headers)
    
    print("🔹 Response status:", response.status_code)
    print("🔹 Response text (first 200 chars):", response.text[:200])
    
    if response.status_code != 200:
        print("❌ API request failed!")
        return
    
    try:
        data = response.json()
    except Exception as e:
        print("❌ JSON parse error:", e)
        return
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for item in data.get("data", []):
            title = item.get("title", "Unknown Channel")
            stream = item.get("stream_url", "")
            f.write(f'#EXTINF:-1 tvg-name="{title}" group-title="Toffee",{title}\n{stream}\n')
    
    print("✅ Playlist generated successfully!")

if __name__ == "__main__":
    api_url = "https://toffeelive.com/api/web/playback/sy5m-JQBv9knK3AHYTTk"
    token = os.getenv("TOFFEE_API_TOKEN")
    
    if not token:
        print("❌ Token missing! Add it to GitHub Secrets (TOFFEE_API_TOKEN)")
    else:
        fetch_toffee_channels(api_url, "toffee_playlist.m3u", token)
