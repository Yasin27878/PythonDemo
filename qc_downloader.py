import requests

url = "http://api.quancai360.com/app/2.0/app/data/api/index"
data1 = "3Ga8tvRrfq0tlU42R2IsJMiXya85q_VLbmSX0_cbLfA.      INL01j0000287a"
data2 = {"iSearch": "IS0002", "deviceId": "ffffffff-a4b9-ddfb-d803-e98856678e3c",
         "sortSymbol": "desc", "sortSellCount": "1", "mac": "bc757459a712", "net": "wifi",
         "cityCode": "310100", "sortPrice": "1", "naviHsid": "232", "isAgent": "0",
         "geolocation": "", "version": "2.2.6", "osVersion": "7.0", "ip": "192.168.100.132",
         "p": "TidLjHwHg6Vm99yxlmsu9AIR2Ac6XxAYqZmzBZmzhKs."}
req = requests.post(url, data=data1 + data2)
print req.text

