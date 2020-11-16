from jikanpy import Jikan #pip install jikanpy
import random
import time

class Searcher:

    #def __init__(self, yearlist, seasonlist, genrelist):
    #    self.yearlist = yearlist
    #    self.seasonlist = seasonlist
    #    self.genrelist = genrelist
    #    self.id = id

    anlist = list()
    def search(self, yearlist, seasonlist, genrelist):
        global anlist
        jikan = Jikan()
        count = 0
        animelist = list()
        #sorts the result by year >> season >> genre >> titles
        for years, seasons in [(years, seasons) for years in yearlist for seasons in seasonlist]: #loops through each item in seasons for each item in yesrs
            results = jikan.season(year = years, season = seasons)
            for result in results['anime']:
                try:
                    start = result['airing_start'].split('-')
                    yearstart = int(start[0])
                except:
                    #print('Unknown year', result['title'], result['airing_start'])
                    yearstart = 0
                if yearstart in yearlist and result['type'] == 'TV':
                    for genres in result['genres']:
                        if genres['name'] in genrelist:
                            if result['mal_id'] not in animelist:
                                animelist.append(result['mal_id'])
                                count += 1
            time.sleep(2)#so twats dont get banned cus rate limiting is an ass
                                #print(f"Title: {result['title']} | mal_id: {result['mal_id']} | airing = {result['airing_start']} | season = {results['season_name']} | type = {result['type']} | genre = {genres['name']}")

        print('number of anime: ', count)
        anlist = animelist
        return animelist


    def idResult(self, id):
        jikan = Jikan()
        result = jikan.anime(id) #want: trailer_url, image_url, url (MAL), title, title_english, status, aired['from' and 'to'].split(T) and get [0] OR premiered, synopsis, score
        answer = f"Title: {result['title']} \nPremiered: {result['premiered']} \nScore: {result['score']} \nAired:{result['premiered']} \nSynopsis: {result['synopsis']}"
        return answer
        #print(f"Title: {result['title']} \nPremiered: {result['premiered']} \nScore: {result['score']} \nAired:{result['premiered']} \nSynopsis: {result['synopsis']}")

    def picker(self, anilist):
        nAnime = len(anilist) - 1
        pick = random.randint(0,nAnime)
        animeid = anilist[pick]
        print('ID:', animeid)
        answer = Searcher.idResult(self,animeid)
        return answer

    def reroll(self):
        global anlist
        Searcher.picker(self, anlist)


#TESTING STUFF
#g = ['Ecchi']
#y = [2010,2011,2020]
#x = ['winter','summer','spring']
#s = Searcher()


#alist = s.search(yearlist = y, seasonlist = x, genrelist = g)
#finale = s.picker(alist)
#print(finale)



#Dictionary parameters: mal_id, url, title, image_url, synopsis, type, airing_start (returns a string like this: '2018-07-05T15:55:00+00:00'), episodes, genres (returns a list)
