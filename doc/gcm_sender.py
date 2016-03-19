import json, urllib2
from tornado.httpclient import AsyncHTTPClient

def make_request(alert_type, ticker, msg_data, reg_ids, link):
    json_data = {
        "collapse_key": alert_type,
        "data" : {
            "data": msg_data,
            "ticker": ticker,
            "link": link,
        }, 
        "registration_ids": reg_ids,
    }


    url = 'https://android.googleapis.com/gcm/send'
    myKey = "" 
    data = json.dumps(json_data)
    headers = {'Content-Type': 'application/json', 'Authorization': 'key=%s' % myKey}
    req = urllib2.Request(url, data, headers)
    f = urllib2.urlopen(req)
    response = json.loads(f.read())


    return json.dumps(response,sort_keys=True, indent=2)

#make_request("Anuradha")
def handle_request(response):
    if response.error:
        print "Error:", response.error
    else:
        print response.body

def make_request1(alert_type,ticker,msg_data,reg_ids,link):
    json_data = {
        "collapse_key" : alert_type, 
        "data" : {
            "data": msg_data,
            "ticker" : ticker,
            "link" : link,
        }, 
        "registration_ids": reg_ids,
    }


    url = 'https://android.googleapis.com/gcm/send'
    myKey = "" 
    data = json.dumps(json_data)
    headers = {'Content-Type': 'application/json', 'Authorization': 'key=%s' % myKey}
    
    http_client = AsyncHTTPClient()
    yield http_client.fetch(url, handle_request, data, headers)




     make_request("Thank you Note! ~%s"%users["name"],"Thank you for letting us know!",
    "Thanks for posting %s"%(event["name"]),[androids["reg_id"]],"findergpstracking://gpstracking#/app/setup")
