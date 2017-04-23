from urllib.request import Request, urlopen
import time
while True:
	req = Request('https://api.bitfinex.com/v1/pubticker/btcusd', headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	callback=urlopen(Request('http://192.168.0.15/text?=' + 'D' + webpage.decode('utf-8'), headers={'User-Agent': 'Mozilla/5.0'})).read()
	print(callback)
	time.sleep(2)
print ("Bye")