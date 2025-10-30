import os
import requests

def fetch_toffee_channels(api_url, output_file, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_url, headers=headers)

    print("🔹 Status Code:", response.status_code)
    print("🔹 Raw Response (first 200 chars):", response.text[:200])

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
            if stream:
                f.write(f'#EXTINF:-1 tvg-name="{title}" group-title="Toffee",{title}\n{stream}\n')

    print("✅ Playlist generated successfully!")

if __name__ == "__main__":
    api_url = "https://toffeelive.com/api/web/playback/sy5m-JQBv9knK3AHYTTk"

    # 👉 এখানে টোকেন বসাও (Secrets ব্যবহার না করলে)
    token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL3RvZmZlZWxpdmUuY29tIiwiY291bnRyeSI6IkJEIiwiZF9pZCI6IjFhNGJiOTAzLWY5MjAtNDZmYS04ZTQyLTExNDVkOTYyMDg4YiIsImV4cCI6MTc2NDQ2MzYwOCwiaWF0IjoxNzYxODMzODA4LCJpc3MiOiJ0b2ZmZWVsaXZlLmNvbSIsImp0aSI6ImU3YTI5OThkLTM4YjctNGI5My05ZmMwLTQ5NzliYzM4MzYzNF8xNzYxODMzODA4IiwicHJvdmlkZXIiOiJ0b2ZmZWUiLCJyX2lkIjoiMWE0YmI5MDMtZjkyMC00NmZhLThlNDItMTE0NWQ5NjIwODhiIiwic19pZCI6IjFhNGJiOTAzLWY5MjAtNDZmYS04ZTQyLTExNDVkOTYyMDg4YiIsInRva2VuIjoiYWNjZXNzIiwidHlwZSI6ImRldmljZSJ9.YqGvOdawMelRRej_Cb9ZdvtaypgWkgaabXd8lGnrLbi0VKvwzw1csEr3CIYkyqeu-ARUVoYIR_Cr8F1cVN-b_w"

    if not token or token.strip() == "":
        print("❌ Token missing! Please add token inside script.")
    else:
        fetch_toffee_channels(api_url, "toffee_playlist.m3u", token)
