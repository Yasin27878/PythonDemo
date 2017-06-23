# This Python file uses the following encoding: utf-8
import sys
import xlsxwriter
import datetime
import time
from openpyxl import load_workbook

reload(sys)
sys.setdefaultencoding('utf-8')

today = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
# 用当前时间减去一天的秒数 得到昨天的时间
yesterday = datetime.datetime.fromtimestamp(time.time() - 86400).strftime('%Y-%m-%d')
print today
print yesterday
t_work = load_workbook(today + ".xlsx")
y_work = load_workbook(yesterday + ".xlsx")
t_sheet = t_work.get_sheet_by_name('Sheet1')
y_sheet = y_work.get_sheet_by_name('Sheet1')
# 获取表格所有行和列，两者都是可迭代的
t_rows = t_sheet.rows
y_rows = y_sheet.rows
for t_row in t_rows:
    ##当前商品ID
    curr_goods_id = t_row[0].value
    # 当前商品属性ID
    curr_product_id = t_row[1].value
    # 当前商品属性对应的价格
    curr_product_price = t_row[4].value
    for y_row in y_rows:
        goods_id = y_rows[0].value
        if curr_goods_id == goods_id:

