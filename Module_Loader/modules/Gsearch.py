import sys
import subprocess
from googlesearch import search
import os
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
os.chdir("/home/badboy17g/HackoHolics/Module_Loader/modules")


a = []
urls = []
s_term=r.get("Query")
s_term = s_term.decode("utf-8")




res = s_term

print(res)

for url in search(res, stop=5):
    urls.append(url)
    
subprocess.call('firefox --new-tab -url '+urls[0]+' --new-tab -url '+urls[1]+' --new-tab -url '+urls[2]+' --new-tab -url '+urls[3]+' --new-tab -url '+urls[4] , shell=True)     
