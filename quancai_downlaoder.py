# This Python file uses the following encoding: utf-8
import datetime
import httplib2
import json
import sys
import xlsxwriter

import goods_downloader
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def get_categroy_data(categtre_id):
    data1 = '3Ga8tvRrfq0tlU42R2IsJLnWoxRFUis-gtlmO0PVXu8.      INL01j0000287a{"iSearch":"IS0002","deviceId":' \
            '"ffffffff-a4b9-ddfb-d803-e98856678e3c","sortSymbol":"desc","sortSellCount":"1","mac":"bc757459a712",' \
            '"net":"wifi","cityCode":"310100","sortPrice":"1","naviHsid":"'
    data2 = '","isAgent":"0","geolocation":"",' '"version":"2.2.6","osVersion":"7.0","ip":"192.168.100.132",' \
            '"p":"TidLjHwHg6Vm99yxlmsu9BQDM98MQMlUFy3zp-rR7nc."}'
    url = "http://api.quancai360.com/app/2.0/app/data/api/index"
    h = httplib2.Http(".cache")
    req, content = h.request(url, "POST", data1 + categtre_id + data2)

    # print req
    # print content
    json_str = content[13:-1] + '}'
    # print json_str
    json_data = json.loads(json_str)
    # print  json_data
    req_code = json_data["returnCode"]

    if req_code == 'AAAAAAA':
        print "获取分类数据成功!"
        categrey_data = json_data["data"]
        # time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S')

        print "商品ID: " + ", 商品名称: " + ", 商品规格: " + ", 商城价格: " + ", 代理商价格: ¥" + ", 打折价格: ¥" + ", 所在城市 " + " ,产品图片 "
        for categrey_1 in categrey_data:

            # goods_downloader.get_goods_price(1002)
            for scen_goods in categrey_1["secondNaviList"]:
                # categrey_1["secondNaviList"].reverse()
                # print "商品ID: " + str(categrey_1['secondNaviHsid']) + " 商品名称: " + str(scen_goods['displayName']) + " 商品价格: ¥" + str(scen_goods['marketPrice'])
                sid = scen_goods['spuHsid']
                goods_downloader.get_goods_price(sid, worksheet)


    else:
        print "获取分类数据失败!"
    pass

workbook = xlsxwriter.Workbook("qc.xlsx")
worksheet = workbook.add_worksheet("type1")
# Start from the first cell. Rows and columns are zero indexed. 按标号写入是从0开始的，按绝对位置'A1'写入是从1开始的
row = 0
col = 0
item_type = ["商品ID", "商品名称 ", "商品规格 ", "商城价格 ", "代理商价格", " 打折价格", " 所在城市", " 产品图片"]
for i in item_type:
    worksheet.write(row, col, i)
    col += 1
row = row + 1

# 210->水管  214->电类  230->泥类 222->木类  232->油类 137->差价
item_categroy = ["210", "214", '230', '222', '232']
for it in item_categroy:
    get_categroy_data(it)
workbook.close()
