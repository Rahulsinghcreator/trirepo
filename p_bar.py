import time
import math
import os
from Easy_F import hrb,hrt
from pyrogram.errors import FloodWait

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False
# 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇
timer = Timer()
async def progress_bar(current,total,reply,start):
      if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            remaining_bytes = total - current
            if speed > 0:
                eta_seconds = remaining_bytes / speed
                eta = hrt(eta_seconds, precision=1)
            else:
                eta = "-"
            sp=str(hrb(speed))+"ps"
            tot=hrb(total)
            cur=hrb(current)
            bar_length = 11
            completed_length = int(current * bar_length / total)
            remaining_length = bar_length - completed_length
            progress_bar = "■" * completed_length + "□" * remaining_length
            
            try:
                await reply.edit(f'╭──⌈📤 𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜 📤⌋──╮ \n├{progress_bar}\n├ 𝙎𝙥𝙚𝙚𝙙⚡ : {sp} \n├ 𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨🧭 : {perc} \n├ 𝙇𝙤𝙖𝙙𝙚𝙙🗂️ : {cur}\n├ 𝙎𝙞𝙯𝙚📭 :  {tot} \n├ 𝙀𝙏𝘼⏳: {eta} \n╰────⌈S A K S H A M⌋───╯\n') 
            except FloodWait as e:
                time.sleep(e.x)
                time.sleep(e.x)
