import asyncio
import telegram
import random
import requests
import os
import time
from datetime import datetime


TOKEN = '1384839096:AAGWot30iO4fFoGJLfG-HdGlVZAksT60noQ'
update_id = "828437023"


async def main():
    global TOKEN
    global update_id
    bot = telegram.Bot(TOKEN)
    async with bot:
        try:
            update = (await bot.get_updates())[-1]
            if str(update.update_id) == update_id:
                print("暂无更新内容")
            else:
                update_id = str(update.update_id)
                try:
                    file_name = update.message.document.file_name
                except AttributeError as e:
                    file_name = "tg_" + "".join(random.sample('zyxwvutsrqponmlkjihgfedcba', 12)) + ".jpg"
                print(file_name)
                # 判断tg压缩图片还是上传图片
                try:
                    file_id = update.message.document.file_id
                except AttributeError as e:
                    file_id = update.message.photo[-1]["file_id"]
                download_link = await bot.get_file(file_id)
                # 同步远端github
                os.system("git fetch --all && git reset --hard origin/main && git pull")
                # 下载图片
                with open("/root/img2github/npm_image_url/rawimg/" + file_name, "wb+") as f:
                    f.write(requests.get(download_link.file_path).content)

                # 修改版本号
                currentDateAndTime = datetime.now()
                year = str(currentDateAndTime.month)
                month = currentDateAndTime.month
                if month < 10:
                    month = "0" + str(month)
                else:
                    month = str(month)
                day = currentDateAndTime.day
                if day < 10:
                    day = "0" + str(day)
                else:
                    day = str(day)

                hour = currentDateAndTime.hour
                if hour < 10:
                    hour = "0" + str(hour)
                else:
                    hour = str(hour)
                minute = currentDateAndTime.minute
                if minute < 10:
                    minute = "0" + str(minute)
                else:
                    minute = str(minute)


                package_json = """{
                    "name": "w2r",
                    "version": "year.month_day.hour_minute",
                    "description": "版本配置文件，每次图片发布后github action会自动修改",
                    "author": "cherbim"
                    }""".replace("year", year).replace("month_day", month + day).replace("hour_minute", hour + minute)
                with open("/root/img2github/npm_image_url/package.json", "w") as f:
                    f.write(package_json)
                # push到github
                os.system("git add ./")
                os.system("git commit -m img2github ./")
                os.system("git push")
                # 删除本地文件
                os.remove("/root/img2github/npm_image_url/rawimg/" + file_name)

        except IndexError as e:
            pass


if __name__ == '__main__':
    while True:
        try:
            asyncio.run(main())
            time.sleep(10)
        except IndexError as e:
            pass
        # 批量更新图片
