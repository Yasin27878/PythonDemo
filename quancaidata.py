import urllib
import urllib2

testdata_header = "3Ga8tvRrfq0tlU42R2IsJMiXya85q_VLbmSX0_cbLfA.      INL01j0000287a"
testdata = {"iSearch": "IS0002", "deviceId": "ffffffff-a4b9-ddfb-d803-e98856678e3c",
            "sortSymbol": "desc", "sortSellCount": "1", "mac": "bc757459a712", "net": "wifi",
            "cityCode": "310100", "sortPrice": "1", "naviHsid": "232", "isAgent": "0",
            "geolocation": "", "version": "2.2.6", "osVersion": "7.0", "ip": "192.168.100.132",
            "p": "TidLjHwHg6Vm99yxlmsu9AIR2Ac6XxAYqZmzBZmzhKs."}
print  urllib.urlencode(testdata)
testdata_urlencode = testdata_header + urllib.urlencode(testdata)
url_data='3Ga8tvRrfq0tlU42R2IsJLnWoxRFUis-gtlmO0PVXu8.      INL01j0000287a{"iSearch":"IS0002","deviceId":"ffffffff-a4b9-ddfb-d803-e98856678e3c","sortSymbol":"desc","sortSellCount":"1","mac":"bc757459a712","net":"wifi","cityCode":"310100","sortPrice":"1","naviHsid":"210","isAgent":"0","geolocation":"","version":"2.2.6","osVersion":"7.0","ip":"192.168.100.132","p":"TidLjHwHg6Vm99yxlmsu9BQDM98MQMlUFy3zp-rR7nc."}'
req_url = "http://api.quancai360.com/app/2.0/app/data/api/index"
req = urllib2.Request(url=req_url,data=url_data)
#req.add_data(url_data)
# req.add_data(testdata_header + testdata)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print  res
