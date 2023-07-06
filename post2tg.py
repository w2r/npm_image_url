import os
import sys
import requests

telegram_token = sys.argv[1]
user_id = [2]
publish_id = [3]
# 推送到telegram
for path, dirs, files in os.walk("rawimg/"):
    for f in files:
        requests.get(f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={user_id}&text=" + "https://cdn.jsdelivr.net/npm/w2r@{publish_id}/" + os.path.join(path, f).replace("\\", "/"))
