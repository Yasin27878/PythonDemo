# This Python file uses the following encoding: utf-8
import httplib2
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

data1 = 'OpiOAT_dmQq1fOqwTIZlxy0fs12DH4mQLNALcsdv5hI.      NA001j0000198a{"deviceId":"ffffffff-a4b9-ddfb-d803-e98856678e3c",' \
        '"geolocation":"","mac":"bc757459a712","version":"2.2.6","ip":"192.168.100.132","osVersion":"7.0",' \
        '"net":"wifi","spuHsid":"'
data2 = '","cityCode":"310100","p":"UG2kqBqROR_jdGnFxawIjMlVnJ65fwylK7UVu-6ENpY."}'
req_url = 'http://api.quancai360.com/app/2.0/app/data/api/navigation'

'''
通过商品id获取商品的所有属性的价格
'''
row = 1


def get_goods_price(goods_id, worksheet):
    global row
    data = data1 + str(goods_id) + data2
    # print data
    h = httplib2.Http(".cache")
    req, content = h.request(req_url, "POST", data)
    # print content
    # 去除掉返回数据的前面13个多余字符 其他为正常的json
    json_str = content[13:-1] + '}'
    # 转化成json
    json_data = json.loads(json_str)
    # 网络请求成功 returnCode = AAAAAAA
    if json_data['returnCode'] == 'AAAAAAA':
        # 数据类
        goods_data = json_data['data']

        # 数据类中单位 (数据比较奇怪 有的为空 有的是额定电压)
        # goods_display_productUnit = goods_data['displayProductUnit']
        # 数据类中的服务 好像都是空
        # goods_services = goods_data['services']
        # 数据类中具体商品列表
        goods_list = goods_data['skuList']
        for goods in goods_list:
            id = str(goods['spuHsid'])
            p_id = str(goods['productHsid'])
            name = goods['productName']
            spu = goods['spuName']
            marketPrice = str(goods['marketPrice'])
            agentPrice = str(goods['agentPrice'])
            discountPrice = str(goods['discountPrice'])
            cityName = goods['cityName']
            result = 'productPic' in goods
            if result:
                productPic = goods['productPic']
            else:
                productPic = "无"
                # print "商品ID: " + id + ", 商品名称: " + name + ", 商品规格: " + spu + ", 商城价格: ¥" + marketPrice + ", 代理商价格: ¥" + agentPrice + ", 打折价格: ¥" + discountPrice + ", 所在城市 " + cityName + " ,产品图片 " + productPic
            print id + ", " + p_id + "," + name + ", " + spu + ", " + marketPrice + ", " + agentPrice + ", " + discountPrice + ", " + cityName + " , " + productPic
            item = []
            item.append(id)
            item.append(p_id)
            item.append(name)
            item.append(spu)
            item.append(marketPrice)
            item.append(agentPrice)
            item.append(discountPrice)
            item.append(cityName)
            item.append(productPic)
            # print row
            for index, i in enumerate(item):
                worksheet.write(row, index, i)
            row = row + 1


pass
