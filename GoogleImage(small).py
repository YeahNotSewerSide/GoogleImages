'''
GoogleImage Api
EnotProd
'''
import bs4
import requests

def getIm(req,pages,folder='.\\'):
    page = 0
    count = 0
    while page != pages:
        cont = requests.get('https://www.google.ru/search?q='+req+'&newwindow=1&biw=1406&bih=743&ie=UTF-8&tbm=isch&ei=CPu5XL7xDIeFmwWYuaG4Bw&start='+str(page*20)+'&sa=N')
        dom = bs4.BeautifulSoup(cont.text, 'html.parser')
        
    
        for link in dom.find_all('img'):
            if count == 0:
                count = 1
                continue
            #print(link.get('src'))
            try:
                r = requests.get(link.get('src')).content
                
            except:
                continue
            count = count + 1
            file = open(folder+'Photo('+str(count)+').jpeg','wb')
            file.write(r)
            file.close()
            
        page = page + 1
    
getIm('Anime Hitler',200,folder='.\\AnimeHitler\\')

