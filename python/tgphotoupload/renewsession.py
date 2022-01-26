import os
import shutil
import threading
from typing import List

import schedule as schedule
from telethon.sync import TelegramClient, events
from datetime import datetime, timedelta
from threading import Timer

FLDR = os.getenv('FLDR')
DST_FLDR = os.getenv('DST_FLDR')
DELAY = 5
SESSION = os.getenv('SESSION')
APIID = os.getenv('APIID')
APIHASH = os.getenv('APIHASH')
DIALOGNAME = os.getenv('DIALOGNAME')

with TelegramClient(SESSION, APIID, APIHASH) as client:
  print(client.session.save())
  



