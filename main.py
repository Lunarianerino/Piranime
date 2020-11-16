import tkinter as tk
from AniSearcher import Searcher
import datetime
import time

year = datetime.datetime.today().year #gets a list of years cus im fucking lazy
YEARS = list(range(year, year - 20, -1)) #gets a list of years from 20 years ago c:

seasons = {'Winter': 0, 'Spring': 0, 'Summer': 0, 'Fall': 0}
genreCol = {'Action': 0, 'Adventure': 1, 'Cars': 2, 'Comedy': 0, 'Dementia': 1, 'Demons': 2, 'Mystery': 0, 'Drama': 1, 'Ecchi': 2, 'Fantasy': 0, 'Game': 1, 'Harem': 2,'Hentai': 0, 'Historical': 1, 'Horror': 2, 'Kids': 0, 'Magic': 1, 'Martial Arts': 2, 'Mecha': 0, 'Music': 1, 'Parody': 2, 'Samurai': 0, 'Romance':1, 'School':2,'Sci-Fi': 0, 'Shoujo': 1, 'Shoujo Ai': 2, 'Shounen': 0, 'Shounen Ai': 1, 'Space': 2,'Sports': 0, 'Slice of Life': 1,'Super Power': 2, 'Vampire': 0, 'Yaoi': 1, 'Yuri'
: 2, 'Supernatural': 0, 'Military': 1, 'Police': 2, 'Psychological': 0, 'Thriller': 1, 'Seinen': 2, 'Josei': 0}
genres = {'Action': 0, 'Adventure': 0, 'Cars': 0, 'Comedy': 0, 'Dementia': 0, 'Demons': 0, 'Mystery': 0, 'Drama': 0, 'Ecchi': 0, 'Fantasy': 0, 'Game': 0, 'Harem': 0,'Hentai': 0, 'Historical': 0, 'Horror': 0, 'Kids': 0, 'Magic': 0, 'Martial Arts': 0, 'Mecha': 0, 'Music': 0, 'Parody': 0, 'Samurai': 0, 'Romance': 0, 'School': 0,'Sci-Fi': 0, 'Shoujo': 0, 'Shoujo Ai': 0, 'Shounen': 0, 'Shounen Ai': 0, 'Space': 0,'Sports': 0, 'Slice of Life': 0,'Super Power': 0, 'Vampire': 0, 'Yaoi': 0, 'Yuri'
: 0, 'Supernatural': 0, 'Military': 0, 'Police': 0, 'Psychological': 0, 'Thriller': 0, 'Seinen': 0, 'Josei': 0}
#GUI start
root = tk.Tk()
root.title("Still thinking about it")

#root.maxsize(300,1000)

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10)

#Year Label Frame
yearFrame = tk.LabelFrame(root, text = "Years")
yearFrame.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = 'W')
#yearFrame.pack(side ='top')

#Season label Frame
seasonFrame = tk.LabelFrame(root, text = "Seasons")
seasonFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = 'W')
#seasonFrame.pack(side = 'top')

#Genre Label Frame
genreFrame = tk.LabelFrame(root, text = "Genres", pady = 20)
genreFrame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = 'W')
#genreFrame.pack(side = 'top', expand = 'true')

submitFrame = tk.LabelFrame(root, text = 'Submit', pady = 20)
submitFrame.grid(row = 2, column = 1, padx = 10, pady = 10, sticky ='NW')

#For Initial Year DropBox
iYearVAR = tk.IntVar(root)
iYearVAR.set(YEARS[0])
iYearLabel = tk.Label(yearFrame, text = 'From: ', anchor = 'w', fg = 'white')
iYearLabel.grid(row = 1, column = 0, padx = (10,0), pady = 10)
#iYearLabel.pack(side = 'left', padx = (20, 2))
iYearDB = tk.OptionMenu(yearFrame, iYearVAR, *YEARS)
iYearDB.grid(row = 1, column = 1, padx = (5,0))
#iYearDB.pack(side = 'left')

#For Final Year DropBox
fYearVAR = tk.IntVar(root)
fYearVAR.set(YEARS[0])
fYearLabel = tk.Label(yearFrame, text = 'To: ', anchor = 'w', fg = 'white')
fYearLabel.grid(row = 1, column = 2, padx = (10,0), pady = 10)
#fYearLabel.pack(side = 'left', padx = (20, 2))
fYearDB = tk.OptionMenu(yearFrame, fYearVAR, *YEARS)
fYearDB.grid(row = 1, column = 3, padx = (5,10))
#fYearDB.pack(side= 'left', padx = (0,20))

#For Seasons Checklist
c = 0
for season in sorted(seasons):
    seasons[season] = tk.IntVar(root)
    s = tk.Checkbutton(seasonFrame, text=season, variable=seasons[season], fg = 'white')
    s.grid(row = 0, column = c, padx = 5, pady = 10)
#    s.pack(side = 'left', padx = (0,6))
    c+=1

columns = [1,2,3]
rows = [1,2,3]
#For Genres Checklist

row = 0
rrow = 0
for genre in genres:
    genres[genre] = tk.IntVar(root)
    g = tk.Checkbutton(genreFrame, text=genre, variable=genres[genre], fg = 'white')
    g.grid(row = row, column = genreCol[genre], padx = 1, pady = 1, sticky = 'w')
    rrow+=1
    if rrow == 3:
        rrow = 0
        row += 1

#        g2.pack(padx = (0,6), anchor = tk.S)

    #print(x)

def getValues():
    global iYearVAR, fYearVAR, seasons
    s = Searcher()
    initialYear = iYearVAR.get()
    finalYear = fYearVAR.get()
    ylist = list(range(initialYear,(finalYear + 1)))
    slist = list()
    glist = list()

    for season in seasons.keys():
        seasons[season] = seasons[season].get()
        svalue = seasons.get(season)
        if svalue == 1:
            slist.append(season)

    for genre in genres.keys():
        genres[genre] = genres[genre].get()
        gvalue = genres.get(genre)
        if gvalue == 1:
            glist.append(genre)

    print(ylist, slist, glist)

    searchResult = s.search(yearlist = ylist, seasonlist = slist, genrelist = glist)
    results = s.picker(searchResult)
    print(results)

submit = tk.Button(submitFrame, text = "Submit", command=getValues)
submit.grid(row = 0, column = 0, padx = 20, pady = 10)
#submit.pack()

#frame=tk.Frame(root, width=300, height=400)
#frame.pack()

root.mainloop()
#alist = s.search(yearlist = y, seasonlist = x, genrelist = g)
#id = s.picker(alist)
#finale = s.idResult(id)
#print(finale)
