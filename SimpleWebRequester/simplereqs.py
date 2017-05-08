import requests
import sys

## single http requester
#url = 'http://192.168.190.128/control'
#r = requests.get(url)
#print url+' size : '+str(len(r.content))

urls = sys.argv[1]
with open(urls,'rb') as f:
	for url in f:
		r = requests.get(url[:-1])
		print url.strip()+' size '+str(len(r.content))
