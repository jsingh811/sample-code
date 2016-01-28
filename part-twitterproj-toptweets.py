import urllib
import httplib
import json
import datetime, time
import os


if os.path.exists("top_tweets.txt"):
 os.remove("top_tweets.txt")
 #########   create UNIX timestamps
start_date = datetime.datetime(2015,02,01, 17,40,0)
end_date = datetime.datetime(2015,02,01, 18,50,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple())) 
 
API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

#########   set query parameters
params = urllib.urlencode({'apikey' : API_KEY, 'q' :'#Patriots',
                           'mintime': str(mintime), 'maxtime': str(maxtime),
                           'new_only': '1', 'include_metrics':'1', 'limit': 5})
#########   create and send HTTP request
req_url = url + '?' + params
req = httplib.HTTPConnection(host)
req.putrequest("GET", req_url)
req.putheader("Host", host)
req.endheaders()
req.send('')


#########   get response and print out status
resp = req.getresponse()
print resp.status, resp.reason


#########   extract tweets
resp_content = resp.read()
ret = json.loads(resp_content)
tweets = ret['response']['results']['list']
for tweet in tweets:
 top5=open("top_tweets.txt","a")
 jsondata = json.dumps(tweet)
 top5.write(jsondata + "\n")
 top5.close()
 
