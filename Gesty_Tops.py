import lxml
import urllib2
import time
import webbrowser
import os
import urllib
import requests
import pafy
from bs4 import BeautifulSoup

print "      GENEROS        "
print "20   - Top Alternative"
print "2    - Top Blues"
print "4    - Top Children's Music"
print "22   - Top Christian & Gospel"
print "5    - Top Classical"
print "3    - Top Comedy"
print "6    - Top Country"
print "17   - Top Dance"
print "7    - Top Electronic"
print "50   - Top Fitness & Workout"
print "18   - Top Hip-Hop/Rap"
print "8    - Top Holiday"
print "11   - Top Jazz"
print "12   - Top Latino"
print "14   - Top Pop"
print "15   - Top R&B/Soul"
print "24   - Top Reggae"
print "21   - Top Rock"
print "16   - Top Soundtrack"
print "19   - Top World"
print
genre = raw_input("Genero de descarga: ")
archivoDescargar = "https://itunes.apple.com/us/rss/topsongs/limit=25/genre=" + genre + "/explicit=true/xml"
archivoGuardar = "list.xml"
print
now = time.time()
 
descarga = urllib2.urlopen(archivoDescargar)
 
ficheroGuardar=file(archivoGuardar,"w")
ficheroGuardar.write(descarga.read())
ficheroGuardar.close()
 
elapsed = time.time() - now

from lxml import etree
doc = etree.parse('list.xml')

for i in range(8, 33):
    raiz=doc.getroot()
    entrada=raiz[i]
    title=entrada[2]
    print (i - 7), " - ", title.text
print
op = raw_input("Desea descargar de alguna cancion? (S/N)")
if op == "S":
    print
    num = input("Cual es el numero de esta:")
    num = num + 7
    st=raiz[num]
    tit=st[2]
    scrape_url="http://www.youtube.com/results?search_query="
    search = tit.text
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
else:
    os.system('cls' if os.name=='nt' else 'clear')
