import tkinter as tk
from AniSearcher import Searcher
from urllib.request import urlopen
import base64
from io import BytesIO
from PIL import Image, ImageTk
import webbrowser

#https://aniwatch.me/search?f=0&a=%5B2%5D&type=%5B0%5D&status=%5B0%5D&e=0&y=%5B1965,2022%5D&o=title&q=[YOUR%20TITLE]
#https://nyaa.si/?f=0&c=0_0&q=[YOUR+TITLE]
class Results:
    def __init__(self, results):

        self.root = tk.Tk()
        self.root.title("Result")

        self.main_frame = tk.Frame(self.root, background = '#232424')
        self.main_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

        #AnimeFrame
        self.textFrame = tk.LabelFrame(self.root, text = "Anime", background = '#333332')
        self.textFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = 'W')

        #Sites
        self.siteFrame = tk.LabelFrame(self.root, text = "Sites", background = '#333332')
        self.siteFrame.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'W')

        #For Cover Image
        self.cover = self.getImage(results['image_url'])
        self.photo = ImageTk.PhotoImage(self.cover)
        self.imgLabel = tk.Label(self.root, image=self.photo)
        self.imgLabel.image = self.photo
        self.imgLabel.grid(row = 0, column = 0, padx = 20, pady = 20)

        #Results Panel
        self.Title = tk.Label(self.textFrame, text = f"Title: {results['title']}", anchor = 'n', fg = 'white', background = '#333332')
        self.Title.grid(row = 0, column = 0, padx =20, pady = 5, sticky = 'W')
        self.Premiered = tk.Label(self.textFrame, text = f"Premiered: {results['premiered']}", anchor = 'n', fg = 'white', background = '#333332')
        self.Premiered.grid(row = 1, column = 0, padx = 20, pady = 5, sticky = 'W')
        self.Score = tk.Label(self.textFrame, text = f"Score: {results['score']}", anchor = 'n', fg = 'white', background = '#333332')
        self.Score.grid(row = 2, column = 0, padx = 20, pady = 5, sticky = 'W')
        self.Synopsis = tk.Label(self.textFrame, text = f"Synopsis:\n{results['synopsis']}", anchor = 'n', fg = 'white', wraplength = 250, justify = tk.LEFT, background = '#333332')
        self.Synopsis.grid(row = 3, column = 0, padx = 20, pady = 5, sticky = 'W')

        #ReRoll button
        self.rerollphoto = tk.PhotoImage(file=r".\icons\reroll.png")
        self.rerollresize = self.rerollphoto.subsample(12,12)
        self.Reroll = tk.Button(self.root, text = 'Re-Roll', image = self.rerollresize, compound = tk.LEFT, command = lambda:[self.refresh(),self.reroll(results)], anchor = 'n', width = 120)
        self.Reroll.grid(row = 1, column = 0, padx = (10,0), pady = 5)

        #AniWatch button
        self.aniwatchp = tk.PhotoImage(file=r".\icons\aniwatch.png")
        self.aniwatchresize = self.aniwatchp.subsample(2,2)
        self.Aniwatch = tk.Button(self.siteFrame, image = self.aniwatchresize, command = lambda:[self.sitequery(query = results['title'], space = '%20'), self.callback(f'https://aniwatch.me/search?f=0&a=%5B2%5D&type=%5B0%5D&status=%5B0%5D&e=0&y=%5B1965,2022%5D&o=title&q={splitquery}')], anchor = 'n')
        self.Aniwatch.grid(row = 0, column = 0, padx = (10,0), pady = 5)

        #nyaa.si button
        self.nyaasip = tk.PhotoImage(file=r".\icons\nyaasi.png")
        self.nyaasiresize = self.nyaasip.subsample(1,1)
        self.Nyaasi = tk.Button(self.siteFrame, image = self.nyaasiresize, command = lambda:[self.sitequery(query = results['title'], space = '+'), self.callback(f'https://nyaa.si/?f=0&c=0_0&q={splitquery}')], anchor = 'n')
        self.Nyaasi.grid(row = 0, column = 1, padx = (10,0), pady = 5)


    def getImage(self, url):
        imageurl = urlopen(url)
        image = imageurl.read()
        imageurl.close()
        img = Image.open(BytesIO(image))
        return img

    def reroll(self, list):
        global rerollres
        rerollres = Searcher.reroll(list)
        self.__init__(rerollres)
        return rerollres

    def refresh(self):
        self.root.destroy()

    def sitequery(self, query, space):
        global splitquery
        splitquery = query.replace(' ', space)
        return splitquery


    def callback(self, url):
        webbrowser.open(url)
