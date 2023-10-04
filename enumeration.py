import os
import requests as rq
import colorama as co
import threading as th
import time
import progressbar as bar


words=[]
info=[]
headers=[]
lists=[]
extensions=['php','txt','bak','html',]
def load_wordlist():
    global words
    dir = os.path.dirname(__file__)
    file=open(dir+'/wordlist.txt','r')
    hilos=os.cpu_count()-1
    cont=0
    words=file.read(100).splitlines()
    size=len(words)/hilos
    if not float.is_integer(size):
        size+=1
         
    for hi in range(hilos):
        for index in range(size):
            for word in words:
                 list[hi].append(word)
                 words.remove(word)
            
           
        
        words.append()
    
    
def enumerate(url):
    global info
    url=str(url)
    
        
    if not url.endswith('/'):
        url=url+"/"
    ses=rq.Session()

    resp=ses.get(url)
    
    
    size=len(words)

    text=resp.status_code
    barra=bar.ProgressBar(max_value=size,)
    barra.enable_colors=True
    barra.init()
    if text==200:
        for word in words:
            res=0
            
            time.sleep(0.01)
            resp=ses.get(url+word)
            if not resp.status_code == 404:
                info.append(resp.url)
                print(resp.url)
            t2=time.ctime()    
            barra.increment()    
    
    
    
if __name__== '__main__':
    
    t=th.Thread(target=load_wordlist)
    t.daemon=True
    t.start()
    
    url=input('Url to enumerate (string) -> ')
    
    t.join()
    
        
    enumerate(url)
    