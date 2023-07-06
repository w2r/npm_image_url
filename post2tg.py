import os
import sys
import requests

telegram_token = os.environ["telegram_token"]
user_id = os.environ["user_id"]
# 获得publish_id
with open("package.json", "r") as f:
    publish_id = f.readlines()[2][14:20]
    print(publish_id)
    print(sys.argv[1])
    print(sys.argv[2])
# 推送到telegram
for path, dirs, files in os.walk("rawimg/"):
    for f in files:
        print(f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={user_id}&text=" + f"https://cdn.jsdelivr.net/npm/w2r@{publish_id}/" + os.path.join(path, f).replace("\\", "/"))
        requests.get(f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={user_id}&text=" + f"https://cdn.jsdelivr.net/npm/w2r@{publish_id}/" + os.path.join(path, f).replace("\\", "/"))
