import os
import sys
import requests

telegram_token = sys.argv[1]
user_id = [2]

# 获得publish_id
with open("package.json", "r") as f:
    publish_id = f.readlines()[3][18:23]
    print(publish_id)
# 推送到telegram
for path, dirs, files in os.walk("rawimg/"):
    for f in files:
        print(f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={user_id}&text=" + "https://cdn.jsdelivr.net/npm/w2r@{publish_id}/" + os.path.join(path, f).replace("\\", "/"))
        requests.get(f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={user_id}&text=" + "https://cdn.jsdelivr.net/npm/w2r@{publish_id}/" + os.path.join(path, f).replace("\\", "/"))
