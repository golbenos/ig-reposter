import requests
import json

with open("config.json") as f:
    config = json.load(f)

ACCESS_TOKEN = config["access_token"]
IG_USER_ID = config["ig_user_id"]

# STEP 1: Upload video URL (replace with your URL or use public Dropbox/Drive/S3)
video_url = "https://example.com/video.mp4"
caption = "🔥 Automatically reposted Reel! #automation #reels"

# 1. Create media container
create_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
params = {
    "media_type": "REELS",
    "video_url": video_url,
    "caption": caption,
    "access_token": ACCESS_TOKEN
}
resp = requests.post(create_url, data=params)
creation_id = resp.json().get("id")

if not creation_id:
    print("❌ Failed to create media container:", resp.text)
    exit()

print("✅ Media container created:", creation_id)

# 2. Publish media
publish_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish"
resp2 = requests.post(publish_url, data={
    "creation_id": creation_id,
    "access_token": ACCESS_TOKEN
})

print("📤 Publish result:", resp2.json())
