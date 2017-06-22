import urllib
import httplib
test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
test_data_urlencode = urllib.urlencode(test_data)
requrl = "http://192.168.81.16/cgi-bin/python_test/test.py"
headerdata = {"Host":"192.168.81.16"}
conn = httplib.HTTPConnection("192.168.81.16")
conn.request(method="POST",url=requrl,body=test_data_urlencode,headers = headerdata)
response = conn.getresponse()
res= response.read()
print res