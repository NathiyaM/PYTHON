import json
from urllib.request import urlopen
url='http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json'
conn=ur.urlopen(url)
print(conn)
