#!/usr/bin/env python
 
import requests
import json
#openssl x509 -x509toreq -in certificate.crt -out CSR.csr -signkey privateKey.key
 
liveKey = ""
delayedKey = ""
footballId = 1
americanFootballID = 6423

payload = 'username=&password='
headers = {'X-Application': delayedKey, 'Content-Type': 'application/x-www-form-urlencoded'}
 
resp = requests.post('https://identitysso.betfair.com/api/certlogin', data=payload, cert=("", ""), headers=headers)
 
if resp.status_code == 200:
  resp_json = resp.json()
  success = True
  sessionToken = resp_json['sessionToken']
  print "Login attempt reply:"
  print "STATUS: " + resp_json['loginStatus']
  print "TOKEN: " + resp_json['sessionToken']
else:
  print "First request failed."
#login code above this
print "--------------------------------"

#
#if success == True:
#	url="https://api.betfair.com/exchange/betting/json-rpc/v1"
#	header = { 'X-Application' : delayedKey, 'X-Authentication' : sessionToken ,'content-type' : 'application/json' }
#	
#	jsonrpc_req = '{"jsonrpc": "2.0","method": "SportsAPING/v1.0/listMarketCatalogue","params": {"filter": {"eventIds": ["27312440"]},"maxResults": "200","marketProjection": ["COMPETITION","EVENT","EVENT_TYPE","RUNNER_DESCRIPTION","RUNNER_METADATA","MARKET_START_TIME"]},"id": 1}'
 
#	response = requests.post(url, data=jsonrpc_req, headers=header)
	 
#	print json.dumps(json.loads(response.text), indent=3)
#else:
#	print "Second request failed."

print "--------------------------------"

if success == True:
	newurl="https://api.betfair.com/exchange/betting/json-rpc/v1"
	newheader = { 'X-Application' : liveKey, 'X-Authentication' : sessionToken ,'content-type' : 'application/json' }
	newjsonrpc_req= '{"jsonrpc": "2.0","method": "SportsAPING/v1.0/listMarketBook","params": { "eventIds" : ["27391856"], "priceProjection":{"priceData":["EX_BEST_OFFERS"]}}, "id": 1}'
	newresponse = requests.post(newurl, data=newjsonrpc_req, headers=newheader)
	print json.dumps(json.loads(newresponse.text), indent=3)
else:
	print "third request failed"

	
	