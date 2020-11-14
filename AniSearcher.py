from jikanpy import Jikan #pip install jikanpy

class Searcher:

    def __init__(self, yearlist, seasonlist, genrelist):
        self.yearlist = yearlist
        self.seasonlist = seasonlist
        self.genrelist = genrelist
        self.id = id

    def search(self, yearlist, seasonlist, genrelist):
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
                            if result['title'] not in animelist:
                                animelist.append(result['title'])
                                count += 1
                                #print(f"Title: {result['title']} | mal_id: {result['mal_id']} | airing = {result['airing_start']} | season = {results['season_name']} | type = {result['type']} | genre = {genres['name']}")

        print('number of anime: ', count)
        return animelist


    def idResult(self, id):
        jikan = Jikan()
        result = jikan.anime(id) #want: trailer_url, image_url, url (MAL), title, title_english, status, aired['from' and 'to'].split(T) and get [0] OR premiered, synopsis, score
        answer = f"Title: {result['title']} \nPremiered: {result['premiered']} \nScore: {result['score']} \nAired:{result['premiered']} \nSynopsis: {result['synopsis']}"
        return answer
        #print(f"Title: {result['title']} \nPremiered: {result['premiered']} \nScore: {result['score']} \nAired:{result['premiered']} \nSynopsis: {result['synopsis']}")
g = ['Action', 'Harem']
y = [2010,2011,2020]
x = ['winter','summer','spring']
s = Searcher(y, seasonlist = x, genrelist = g)

#finale = s.search(yearlist = y, seasonlist = x, genrelist = g)
finale = s.idResult(1)
print(finale)

#Dictionary parameters: mal_id, url, title, image_url, synopsis, type, airing_start (returns a string like this: '2018-07-05T15:55:00+00:00'), episodes, genres (returns a list)
