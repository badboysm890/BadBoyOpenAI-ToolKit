from __future__ import unicode_literals
import urllib.request
from bs4 import BeautifulSoup
import sys
import youtube_dl
import os
import subprocess
import webbrowser
import redis
os.chdir("/home/badboy17g/HackoHolics/Module_Loader/modules")

r = redis.Redis(host='localhost', port=6379, db=0)
# textToSearch = args = sys.argv
# s_term = args[1]

s_term=r.get("Query")
s_term = s_term.decode("utf-8")

query = urllib.parse.quote(s_term)
results = []
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    a = 'https://www.youtube.com' + vid['href']
    results.append(a)

file = "songs/"+s_term+".mp3"
ydl_opts = {
    'outtmpl': file,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    print(results[0])
    a = ydl.download([results[0]])

subprocess.run("killall io.elementary.music", shell=True)
webbrowser.open(file)