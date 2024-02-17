import requests
import json
import subprocess
from pyrogram import Client,filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
from pyrogram import Client, filters
import tgcrypto
from p_bar import progress_bar
# from details import api_id, api_hash, bot_token
from subprocess import getstatusoutput
import helper
import logging
import time
import aiohttp
import asyncio
import aiofiles
from pyrogram.types import User, Message
# import progressor 
# from progressor import progress_for_pyrogram
import sys
import re
import os
from os import environ
# import pycurl

bot = Client(
    "bot",
    bot_token=environ.get('BOT_TOKEN'), 
    api_id=int(environ.get('API_ID')), 
    api_hash=environ.get('API_HASH'),
    workers= 6)


@bot.on_message(filters.command(["help"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Hello Im txt File Downloader\n\n**Steps To Use Bot:**\n **1:** Send /start & then send your .txt file.\n **2:** Now Send From Where You Want To    Download Initial is 0 .\n **3:** Now Send Your File Name or Use 'de' For.  Use Default File Name.\n **4:** Now Send Resolution In Which Quality    You Want.\n **5:** Now Againg Send /start.\n **6:** Now Send Custom Thum URL or    Send 'no'To Use Defalut Thumbnail.\n **7:** Now Wait Bot will Download & Upload Your    Videos.\n\n**Bot made by 🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇**")

@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancelled")
    return
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("**Hi!, I'm PyroBot. \n\nI Can Download All Links In A Txt File & Send Them To You.\n\nUse /help To Get Some Help 😉\n\n Now Send .txt file\n\n BOT MODIFIED BY 『🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇™』**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text


    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    
    editable = await m.reply_text("**Enter Title For File. Send 'de' To Use Default File Name.**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    await m.reply_text("**Enter Video Resolution **")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    
    await editable.edit("**Enter Your Name or send `de` for use default file Name**")

    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    if raw_text3 == 'de':
        CR = credit
    else:
        CR = raw_text3

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/Abhi-04-08```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)    

    
    try:
        for i in range(arg, len(links)):
            
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()



            if raw_text2 =="144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']    
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)              
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"                        

            elif raw_text2 =="240":
                
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)          
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="360":
            
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)             
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']  
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="480":
                
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)               
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']                        
                elif '854x470' in out:
                    ytf = out['854x470']  
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf =['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']   
                elif 'unknown' in out:
                    ytf = out["unknown"]                     
                else:
                    ytf = "no"

                   
            elif raw_text2 =="720":
                
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)           
                if '1280x720' in out:
                    ytf = out['1280x720'] 
                elif '1280x704' in out:
                    ytf = out['1280x704'] 
                elif '1280x474' in out:
                    ytf = out['1280x474'] 
                elif '1920x712' in out:
                    ytf = out['1920x712'] 
                elif '1920x1056' in out:
                    ytf = out['1920x1056']    
                elif '854x480' in out:
                    ytf = out['854x480']                        
                elif '640x360' in out:
                    ytf = out['640x360']     
                elif 'unknown' in out:
                    ytf = out["unknown"]              
                else:
                    ytf = "no"
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf= 'http-240p'
                elif raw_text2 == "240":
                    ytf= 'http-240p'
                elif raw_text2 == '360':
                    ytf= 'http-360p'
                elif raw_text2 == '480':
                    ytf= 'http-540p'
                elif raw_text2 == '720':
                    ytf= 'http-720p'
                else:
                    ytf = 'http-360p'
            else:
                ytf="no"

            if ytf == "0":
                res = "0"
            elif ytf == "no" or ytf == "mp4":
                res = "NA"
            else:
                res = list(out.keys())[list(out.values()).index(ytf)]

            name = f'{name1}'

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6Mzg3Mjg5NzYsIm9yZ0lkIjo4NTQ4LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTg3MDgzODc2NDgiLCJuYW1lIjoiTXVzdHVmYSIsImVtYWlsIjpudWxsLCJpc0ludGVybmF0aW9uYWwiOjAsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImNvdW50cnlJU08iOiI5MSIsInRpbWV6b25lIjoiR01UKzU6MzAiLCJpc0RpeSI6ZmFsc2UsImZpbmdlcnByaW50SWQiOiJiNjVkY2NkZjg2NGE0MGUyZjQyZjQ4YTg2OWYzYzU3MSIsImlhdCI6MTY3MzU3NTkwOSwiZXhwIjoxNjc0MTgwNzA5fQ.c1ZM9_Kzrb4Bmou0c7HNzscPWtBwikdZUCNmv8K0OCo08ySZoktpbhUA9z4DHqRj'}).json()['url']

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'


            if "youtu" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --no-keep-video --remux-video mp4 "{url}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" in url:
                cmd = "pdf"
            elif "drive" in url:
                cmd = "pdf"
            elif ytf == "no":
                cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mp4 "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
                


            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`\n\n"
                prog = await m.reply_text(Show)
                cc = f'**File Name »** {name1} 🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇.mp4\n**Batch »** {raw_text0}\n\n**{CR}**'
                cc1 =f'**File No. »** {str(count).zfill(3)}\n**File Name »** {name1} 🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇.pdf\n**Batch »** {raw_text0}\n\n**{CR}**'
                if cmd == "pdf" or "drive" in url:
                    try:
                        ka=await helper.download(url,name)
                        await prog.delete (True)
                        time.sleep(1)
                        # await helper.send_doc(bot,m,cc,ka,cc1,prog,count,name)
                        reply = await m.reply_text(f"Uploading - `{name}`")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka,caption=cc1)
                        count+=1
                        await reply.delete (True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue                    
                elif cmd == "pdf" or ".pdf" in url:
                    try:
                        ka=await helper.aio(url,name)
                        await prog.delete (True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka, caption=f'**File No. »** {str(count).zfill(3)}\n**File Name »** {name1} 🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇.pdf\n**Batch »** {raw_text0}\n\n**{CR}**')
                        count+=1
                        # time.sleep(1)
                        await reply.delete (True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    res_file = await helper.download_video(url,cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m,cc,filename,thumb,name,prog)
                    count+=1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`")
                continue


    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")    
    
    
    
@bot.on_message(filters.command(["jw"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Send txt file**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text


    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    
    editable = await m.reply_text("**Enter Title**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)    

    
    try:
        for i in range(arg, len(links)):
            
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()
            
            if "jwplayer" in url:
                headers = {
                    'Host': 'api.classplusapp.com',
                    'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0',
                    'user-agent': 'Mobile-Android',
                    'app-version': '1.4.37.1',
                    'api-version': '18',
                    'device-id': '5d0d17ac8b3c9f51',
                    'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30',
                    'accept-encoding': 'gzip',
                }

                params = (
                    ('url', f'{url}'),
                )

                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                # print(response.json())
                a = response.json()['url']
                # print(a)


                headers1 = {
                    'User-Agent': 'ExoPlayerDemo/1.4.37.1 (Linux;Android 11) ExoPlayerLib/2.14.1',
                    'Accept-Encoding': 'gzip',
                    'Host': 'cdn.jwplayer.com',
                    'Connection': 'Keep-Alive',
                }


                response1 = requests.get(f'{a}', headers=headers1)

                url1 = (response1.text).split("\n")[2]
                            
#                 url1 = b
            else:
                url1 = url

                
            name = f'{str(count).zfill(3)}) {name1}'    
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url1}`"
            prog = await m.reply_text(Show)
            cc = f'**Title »** {name1}.mkv\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}'
            if "pdf" in url:
                cmd = f'yt-dlp -o "{name}.pdf" "{url1}"'
            else:
                cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mkv "{url1}"'
            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)
                

                if os.path.isfile(f"{name}.mkv"):
                    filename = f"{name}.mkv"
                elif os.path.isfile(f"{name}.mp4"):
                    filename = f"{name}.mp4"  
                elif os.path.isfile(f"{name}.pdf"):
                    filename = f"{name}.pdf"  
#                 filename = f"{name}.mkv"
                subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
                await prog.delete (True)
                reply = await m.reply_text(f"Uploading - ```{name}```")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e))

                dur = int(helper.duration(filename))

                start_time = time.time()
                if "pdf" in url1:
                    await m.reply_document(filename,caption=cc)
                else:
                    await m.reply_video(filename,supports_streaming=True,height=720,width=1280,caption=cc,duration=dur,thumb=thumbnail, progress=progress_bar,progress_args=(reply,start_time) )
                count+=1
                os.remove(filename)

                os.remove(f"{filename}.jpg")
                await reply.delete (True)
                time.sleep(1)
            except Exception as e:
                await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}` & `{url1}`")
                continue 
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")     
    
bot.run()
