import wx
import urllib
import urllib2
import requests
import pafy
import sys
from bs4 import BeautifulSoup

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)

        # Agregando botones
        self.button1 = wx.Button(self, -1, u"BUSCAR", size=(300,20), pos=(10,10))
        self.button2 = wx.Button(self, -1, u"SALIR", size=(300,20), pos=(10,110))
        self.A = wx.TextCtrl(self, wx.ID_ANY, pos=(10,35), size=(300,20))
        self.st1 = wx.StaticText(self, label=' ', size=(300,20), pos=(10, 65))
        self.st2 = wx.StaticText(self, label='En espera...', size=(300,20), pos=(10, 85))
        self.SetBackgroundColour('#f0f0f0')
        # Conectando el evento de un boton
        self.Bind(wx.EVT_BUTTON, self.OnClick)
        
        # Mostrando la interfaz
        self.Show()
        
    def OnClick(self,event):
        if (event.EventObject.GetLabel())=="BUSCAR":
            scrape_url="http://www.youtube.com/results?search_query="
            search = self.A.GetValue()
            self.st2.SetLabel("Buscando...")
            search_hardcode = search.replace(" ", "+")
            self.st1.SetLabel(search_hardcode)
            sb_url = scrape_url + search_hardcode
            sb_get = requests.get(sb_url)
            soupeddata = BeautifulSoup(sb_get.content, "html.parser")
            yt_links = soupeddata.find_all("a", {"class": "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})
            yt_href = yt_links[0].get("href")
            yt_title = yt_links[0].get("title")
            self.st1.SetLabel(yt_title)
            self.st2.SetLabel("Encontrado...")
            yt_url = 'https://www.youtube.com' + yt_href
            url = yt_url
            video = pafy.new(url)
            best = video.getbest()
            self.st2.SetLabel("Descargando...")
            #print best.url  Se usa para transmitir el video por vlc
            bestaudio = video.getbestaudio()
            pathf = "Musica"
            bestaudio.download(filepath=pathf)
            self.st2.SetLabel("Listo!")
        if (event.EventObject.GetLabel())=="SALIR":
            sys.exit()

            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "GESTY", size=(335,175))
    app.MainLoop()
