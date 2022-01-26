import os
import shutil
import threading
from typing import List

import time
import schedule as schedule
from telethon.sync import TelegramClient, events
from datetime import datetime, timedelta
from threading import Timer


"""
So, this shit works following way: 
We put pics to dir1 manually 
Then this crap indexes pics and filenames and sends 10 pics a day to the channel (btw is 10 enough? dunno)  
Then it puts the pictures that were already sent to dir2 which holds pics that were already sent
+ extra bonus - add /new command for the channel so users could ask for more pics (put a timer there too?)
When pics in dir1 are no more, we send a notification to a meatbag so he puts smore

Algorithms:
(- sort files in the folder by the timestamp added) 
- get all files from a folder
- add them to the image pool
- free 1 picture from the pool in a predetermined period of time (and send it to channel) x10
- if the pool is empty, then re-read the contents of the folder (and send notification) 
"""

FLDR = os.getenv('FLDR')
DST_FLDR = os.getenv('DST_FLDR')
DELAY = 5
SESSION = os.getenv('SESSION')
APIID = os.getenv('APIID')
APIHASH = os.getenv('APIHASH')
DIALOGNAME = os.getenv('DIALOGNAME')


class ImagePool:
    def __init__(self):
        self.image_pool = get_all_images(FLDR)

    def get_images(self) -> List:
        if not self.is_empty():
            if len(self.image_pool) > 5:
                img_list = self.image_pool[-5:]
                del self.image_pool[-5:]
                return img_list
            else:
                img_list = self.image_pool
                self.image_pool = []
                return img_list
        else:
            self.set_new_pool()

    def set_new_pool(self):
        print('adding new files')
        self.image_pool = get_all_images(os.path.abspath(FLDR))
        print(self.image_pool)

    def is_empty(self) -> bool:
        if len(self.image_pool) != 0:
            return False
        else:
            print("this shit is empty fukka")
            #with TelegramClient(SESSION, APIID, APIHASH) as client:
              
            # send fucking message to the meatbag
            # but send it only once plez so not to spam by CD
            # like use a flag that the notification was sent or smthn
            return True


def get_all_images(check_path: str) -> List:
    print("check_path: " + check_path)
    all_images = []
    valid_ext = ["jpg", "jpeg", "gif", "png", "tga"]
    for path, sub_dirs, files in os.walk(check_path):
        for filename in files:
            ext = filename.split('.')[-1]
            if ext.lower() in valid_ext:
                all_images.append(os.path.join(FLDR, filename))
    # sort files by modification date, from oldest to newest
    all_images.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return all_images


def operate_images(img_pool: ImagePool):
    imgs = img_pool.get_images()
    print(imgs)
    if imgs:
        # telethon send img to channel
        with TelegramClient(SESSION, APIID, APIHASH) as client:
            for img in imgs:
# check if image already exists in DST folder
# if it does - discard it 
#                if img exists in DST folder
#                  os.remove(img)
#                  continue
                client.send_file(DIALOGNAME, img)
                if not os.path.exists(DST_FLDR):
                    os.makedirs(DST_FLDR)
                if not os.path.isdir(DST_FLDR):
                    os.remove(DST_FLDR)
                    os.makedirs(DST_FLDR)
                shutil.move(img, DST_FLDR)
                print('file moved')
        print('waiting for the next iteration...')


def time_schedule():
    x = datetime.today()
    y = x.replace(day=x.day, hour=4, minute=0, second=0, microsecond=0) + timedelta(hours=5)
#    y = x + timedelta(hours=3)  # try once per 30 min
    delta_t = y-x
    seconds = delta_t.total_seconds()
    return seconds


def ticker_start(img_pool, secs):
    ticker = threading.Event()
    while not ticker.wait(secs):
        operate_images(img_pool)


if __name__ == '__main__':
    pool = ImagePool()
    # secs = time_schedule()
    # print(secs)
    # ticker_start(pool, secs)
#    t = Timer(secs, ticker_start(pool))
#    t.start()
    # TODO: -> try to use schedule module
    schedule.every().day.at("10:00").do(lambda: operate_images(pool))
    schedule.every().day.at("12:00").do(lambda: operate_images(pool))
    schedule.every().day.at("15:00").do(lambda: operate_images(pool))
    schedule.every().day.at("17:00").do(lambda: operate_images(pool))
    schedule.every().day.at("19:00").do(lambda: operate_images(pool))
    schedule.every().day.at("22:00").do(lambda: operate_images(pool))
    while True:
        schedule.run_pending()
        time.sleep(10)
