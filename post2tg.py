import os
import json
import requests

telegram_token = os.environ["telegram_token"]
user_id = os.environ["user_id"]
cdn_name = os.environ["cdn"]
cdn = {
    "jsdelivr": "https://cdn.jsdelivr.net/npm/",
    "zhimg": "https://unpkg.zhimg.com/",
    "bdstatic": "https://code.bdstatic.com/npm/",
    "eleme": "https://shadow.elemecdn.com/npm/",
    "unpkg": "https://unpkg.com/",
}
# 获得publish_id
with open("package.json", "r") as f:
    publish_version = json.load(f)["version"]
    publish_name = json.load(f)["name"]
# 推送到telegram
for path, dirs, files in os.walk("rawimg/"):
    for f in files:
        if ".webp" in f:
            requests.get(f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={user_id}&text=" + f"{cdn['cdn_name']}{publish_version}@{publish_version}/" + os.path.join(path, f).replace("\\", "/"))
