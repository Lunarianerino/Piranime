import tkinter as tk
from AniSearcher import Searcher
import datetime
import time
from resultWindow import Results



#GUI start

#root.maxsize(300,1000)
class mainWindow:
    def __init__(self):
        self.year = datetime.datetime.today().year #gets a list of years cus im fucking lazy
        self.YEARS = list(range(self.year, self.year - 20, -1)) #gets a list of years from 20 years ago c:

        self.seasons = {'Winter': 0, 'Spring': 0, 'Summer': 0, 'Fall': 0}
        self.genreCol = {'Action': 0, 'Adventure': 1, 'Cars': 2, 'Comedy': 0, 'Dementia': 1, 'Demons': 2, 'Mystery': 0, 'Drama': 1, 'Ecchi': 2, 'Fantasy': 0, 'Game': 1, 'Harem': 2, 'Josei': 0, 'Historical': 1, 'Horror': 2, 'Kids': 0, 'Magic': 1, 'Martial Arts': 2, 'Mecha': 0, 'Music': 1, 'Parody': 2, 'Samurai': 0, 'Romance':1, 'School':2,'Sci-Fi': 0, 'Shoujo': 1, 'Shoujo Ai': 2, 'Shounen': 0, 'Shounen Ai': 1, 'Space': 2,'Sports': 0, 'Slice of Life': 1,'Super Power': 2, 'Vampire': 0, 'Yaoi': 1, 'Yuri': 2, 'Supernatural': 0, 'Military': 1, 'Police': 2, 'Psychological': 0, 'Thriller': 1, 'Seinen': 2}
        self.genres = {'Action': 0, 'Adventure': 0, 'Cars': 0, 'Comedy': 0, 'Dementia': 0, 'Demons': 0, 'Mystery': 0, 'Drama': 0, 'Ecchi': 0, 'Fantasy': 0, 'Game': 0, 'Harem': 0, 'Historical': 0, 'Horror': 0, 'Kids': 0, 'Magic': 0, 'Martial Arts': 0, 'Mecha': 0, 'Music': 0, 'Parody': 0, 'Samurai': 0, 'Romance': 0, 'School': 0,'Sci-Fi': 0, 'Shoujo': 0, 'Shoujo Ai': 0, 'Shounen': 0, 'Shounen Ai': 0, 'Space': 0,'Sports': 0, 'Slice of Life': 0,'Super Power': 0, 'Vampire': 0, 'Yaoi': 0, 'Yuri'
        : 0, 'Supernatural': 0, 'Military': 0, 'Police': 0, 'Psychological': 0, 'Thriller': 0, 'Seinen': 0, 'Josei': 0}

        self.root = tk.Tk()
        self.root.title("AniSearch by Lunaria")

        self.main_frame = tk.Frame(self.root, background = '#232424')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        #Year Label Frame
        self.yearFrame = tk.LabelFrame(self.root, text = "Years | WARNING: Bigger range = Bigger Load Times", background = '#333332')
        self.yearFrame.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = 'W')
        #yearFrame.pack(side ='top')

        #Season label Frame
        self.seasonFrame = tk.LabelFrame(self.root, text = "Seasons", background = '#333332')
        self.seasonFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = 'W')
        #seasonFrame.pack(side = 'top')

        #Genre Label Frame
        self.genreFrame = tk.LabelFrame(self.root, text = "Genres", pady = 20, background = '#333332')
        self.genreFrame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = 'W')
        #genreFrame.pack(side = 'top', expand = 'true')

        self.submitFrame = tk.LabelFrame(self.root, text = 'Submit', pady = 20, background = '#333332')
        self.submitFrame.grid(row = 2, column = 1, padx = 10, pady = 10, sticky ='NW')

        #For Initial Year DropBox
        self.iYearVAR = tk.IntVar(self.root)
        self.iYearVAR.set(self.YEARS[0])
        self.iYearLabel = tk.Label(self.yearFrame, text = 'From: ', anchor = 'w', fg = 'white', background = '#333332')
        self.iYearLabel.grid(row = 1, column = 0, padx = (10,0), pady = 10)
        #iYearLabel.pack(side = 'left', padx = (20, 2))
        self.iYearDB = tk.OptionMenu(self.yearFrame, self.iYearVAR, *self.YEARS)
        self.iYearDB.grid(row = 1, column = 1, padx = (5,0))
        #iYearDB.pack(side = 'left')

        #For Final Year DropBox
        self.fYearVAR = tk.IntVar(self.root)
        self.fYearVAR.set(self.YEARS[0])
        self.fYearLabel = tk.Label(self.yearFrame, text = 'To: ', anchor = 'w', fg = 'white', background = '#333332')
        self.fYearLabel.grid(row = 1, column = 2, padx = (10,0), pady = 10)
        #fYearLabel.pack(side = 'left', padx = (20, 2))
        self.fYearDB = tk.OptionMenu(self.yearFrame, self.fYearVAR, *self.YEARS)
        self.fYearDB.grid(row = 1, column = 3, padx = (5,10))
        #fYearDB.pack(side= 'left', padx = (0,20))

        #For Seasons Checklist
        self.c = 0
        for season in sorted(self.seasons):
            self.seasons[season] = tk.IntVar(self.root)
            self.s = tk.Checkbutton(self.seasonFrame, text=season, variable=self.seasons[season], fg = 'white', background = '#333332')
            self.s.grid(row = 0, column = self.c, padx = 5, pady = 10)
        #    s.pack(side = 'left', padx = (0,6))
            self.c+=1

        #For Genres Checklist
        self.row = 0
        self.rrow = 0
        for genre in self.genres:
            self.genres[genre] = tk.IntVar(self.root)
            self.g = tk.Checkbutton(self.genreFrame, text=genre, variable=self.genres[genre], fg = 'white', background = '#333332')
            self.g.grid(row = self.row, column = self.genreCol[genre], padx = 1, pady = 1, sticky = 'w')
            self.rrow+=1
            if self.rrow == 3:
                self.rrow = 0
                self.row += 1

#        g2.pack(padx = (0,6), anchor = tk.S)

        self.submit = tk.Button(self.submitFrame, text = "Submit",  command=lambda: [self.destroyframe(),self.getValues(),Results(rel)])
        self.submit.grid(row = 0, column = 0, padx = 20, pady = 10)


        self.root.mainloop()

    #print(x)
    def destroyframe(self):
        self.root.destroy()

    def getValues(self):
        global rel
        s = Searcher()
        self.initialYear = self.iYearVAR.get()
        self.finalYear = self.fYearVAR.get()
        self.ylist = list(range(self.initialYear,(self.finalYear + 1)))
        self.slist = list()
        self.glist = list()

        for season in self.seasons.keys():
            self.seasons[season] = self.seasons[season].get()
            self.svalue = self.seasons.get(season)
            if self.svalue == 1:
                self.slist.append(season)

        for genre in self.genres.keys():
            self.genres[genre] = self.genres[genre].get()
            self.gvalue = self.genres.get(genre)
            if self.gvalue == 1:
                self.glist.append(genre)

        print(self.ylist, self.slist, self.glist)
        self.searchResult = s.search(yearlist = self.ylist, seasonlist = self.slist, genrelist = self.glist)
        self.results = s.picker(self.searchResult)
        rel = self.results
        return self.results

firswindow = mainWindow()
