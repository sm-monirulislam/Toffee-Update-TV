import json
import os
import requests

API_BASE = "https://toffeelive.com/api/web/playback/"
JWT_TOKEN = os.getenv("TOFFEE_JWT")

if not JWT_TOKEN:
    raise Exception("❌ Missing TOFFEE_JWT environment variable")

with open("channels.json", "r", encoding="utf-8") as f:
    channels = json.load(f)

m3u_lines = ["#EXTM3U"]

for ch in channels:
    ch_name = ch["name"]
    ch_id = ch["id"]
    url = f"{API_BASE}{ch_id}"

    headers = {
        "User-Agent": "okhttp/4.9.3",
        "Authorization": f"Bearer {JWT_TOKEN}"
    }

    try:
        r = requests.get(url, headers=headers)
        data = r.json()

        stream_url = data.get("data", {}).get("playback_url") or ""
        if stream_url:
            m3u_lines.append(f"#EXTINF:-1,{ch_name}")
            m3u_lines.append(stream_url)
            print(f"✅ Added: {ch_name}")
        else:
            print(f"⚠️ No stream for {ch_name}")

    except Exception as e:
        print(f"❌ Error for {ch_name}: {e}")

with open("toffee_channels.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(m3u_lines))

print("✅ M3U file generated successfully: toffee_channels.m3u")
