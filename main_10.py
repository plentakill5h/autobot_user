from multiprocessing.connection import Client
from tokenize import group
from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sync import TelegramClient
from telethon.tl.types import UserStatusOnline, UserStatusOffline, ContactStatus
from datetime import datetime
from telethon import events
from telethon import TelegramClient, sync
import pandas as pd
from telethon import errors
import time
from ratelimiter import RateLimiter
from telethon import types

#api_id = '11179869' #alanjan
#api_hash = 'ce77400be12d0b39423a631aa3e40869' #alanjan
#phone = '+32498684103'#alanjan

#api_id = '18705515' #milan
#api_hash = '8508c78152469f827b6eddd9f0d3a4b3' #milan
#phone = '+32499136862' #milan

api_id = '15469674' #ari
api_hash = '305527c0c7911610b50f11892c74d12d' #ari
phone = '+32456056118' #ari

with open('/home/ubuntu/Desktop/telegram_bot/files/groups.txt','r') as groupsList:
    groups = groupsList.readlines()

def limited(until):
    duration = int(round(until - time.time()))
    print('Rate limited, sleeping for {:d} seconds'.format(duration))

rate_limiter = RateLimiter(max_calls=1, period=1, callback=limited)

client = TelegramClient('@Arijanblo', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
	client.send_code_request(phone)
	client.sign_in(phone, input('Enter the code: '))

async def main():

    with rate_limiter:
        try:
            await client.start()
            user_details = await client.get_entity(groups)
            time.sleep(6) 
            for i in range(len(user_details)):

                if hasattr(user_details[i], "status"):
                    print(user_details[i].username, user_details[i].status)

            time.sleep(6)

        except errors.FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            time.sleep(e.seconds)

        

time.sleep(20)
with client:
    client.loop.run_until_complete(main())