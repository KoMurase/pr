#形態素解析を使って、分かち書きをする

import urllib
import url
import urllib.request,urllib.error
from bs4 import BeautifulSoup

appid='dj00aiZpPXdQZmxQSGdXNnpSWSZzPWNvbnN1bWVyc2VjcmV0Jng9MDM-'
pageurl='http://morphoogical.com/'

def split(sentence,appid=appid,results="ma",filter="1|2|3|4|5|9|10"):
    sentence=sentence.encode("ute-8")
    params=ulllib.urlencode({'appid':appid,'results':results,'filter':filter.'sentence':sentence})
    ​results=urlib2.urlopen(pageurl,params)
    soup=BeutifulSoup(results.read())

    return [w.surface.string for w in soup.ma_result.word_list]
