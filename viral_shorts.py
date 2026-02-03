import requests
import subprocess
import os

BRIDGE = "https://starsun.site/api"
REPO_ID = "repo-04"
TOKEN = "REPO04_SECRET"

# 1. هل أعمل؟
r = requests.get(f"{BRIDGE}/should_run.php", params={
    "repo": REPO_ID,
    "token": TOKEN
}).json()

if not r["run"]:
    exit()

# 2. البحث عن فيديو (placeholder)
# 3. قص 35 ثانية
# 4. إزالة الصوت
# 5. Whisper → Gemini → TTS (Gemini API KEY يوضع لاحقًا)
# 6. دمج + captions
# 7. إرسال الفيديو للموقع

files = {'video': open('final.mp4','rb')}
requests.post(f"{BRIDGE}/receive_video.php", files=files)
