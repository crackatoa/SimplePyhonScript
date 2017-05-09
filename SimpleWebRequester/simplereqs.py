import requests
import sys

## single http requester
#url = 'http://192.168.190.128/control'
#r = requests.get(url)
#print url+' size : '+str(len(r.content))

green = '\033[1;32m'
red = '\033[1;31m'
end = '\033[0m'
 
urls = sys.argv[1]
with open(urls,'rb') as f:
	for url in f:
		r = requests.get(url[:-1])
		size = len(r.content)
		if size > 0 :
			print green+'[*] '+end+url.strip()+' '+green+'size '+str(size)+end
		else :
			print red+'[*] '+end+url.strip()+' '+red+'size '+str(size)+end
