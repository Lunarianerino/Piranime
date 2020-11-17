import tkinter as tk
from AniSearcher import Searcher
from urllib.request import urlopen
import base64
from io import BytesIO
from PIL import Image, ImageTk
class Results:
    def __init__(self, results):

        self.root = tk.Tk()
        self.root.title("Result")

        self.main_frame = tk.Frame(self.root, background = '#232424')
        self.main_frame.grid(row = 0, column = 0, padx = 10, pady = 10)
        print(results['image_url'])

        #AnimeFrame
        self.textFrame = tk.LabelFrame(self.root, text = "Anime", background = '#333332')
        self.textFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = 'W')

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

        self.Reroll = tk.Button(self.root, text = 'Re-Roll', command = lambda:[self.refresh(),self.reroll(results)], anchor = 'n')
        self.Reroll.grid(row = 1, column = 0, padx = (10,0), pady = 10)




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
