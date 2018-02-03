import urllib
import urllib2
import requests
import pafy
from bs4 import BeautifulSoup

scrape_url="http://www.youtube.com/results?search_query="
search = raw_input("Nombre de la cancion: ")
search_hardcode = search.replace(" ", "+")
sb_url = scrape_url + search_hardcode
sb_get = requests.get(sb_url)
soupeddata = BeautifulSoup(sb_get.content, "html.parser")
yt_links = soupeddata.find_all("a", {"class": "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})
yt_href = yt_links[0].get("href")
yt_title = yt_links[0].get("title")
yt_url = 'https://www.youtube.com' + yt_href
url = yt_url
video = pafy.new(url)
best = video.getbest()
print
print yt_url
print yt_title
print video.duration
#print best.url  Se usa para transmitir el video por vlc
bestaudio = video.getbestaudio()
pathf = "Musica"
bestaudio.download(filepath=pathf)

