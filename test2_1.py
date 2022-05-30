long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
# 这一块和之前从网页提取相反，也就是将数据重新封装

list_dic = []
dic = {}
for i in range(1, len(long_text.split('.'))):
    dic1 = {}
    list_isin = []
    for j in range(1, len(long_text.split('.')[i].split('\n')) - 1):
        dic1['title'] = long_text.split('.')[i].split('\n')[0]
        list_isin.append(long_text.split('.')[i].split('\n')[j])
    dic1['isin'] = list_isin
    list_dic.append(dic1)
    dic['name'] = long_text.split('.')[0].split('\n')[1]
    dic['lei'] = long_text.split('.')[0].split('\n')[2]
    dic['sub_fund'] = list_dic

print(dic)

# 本来直接从txt中用用对应提取再封装，也能遍历。

# coding: utf8
# import numpy as np
#
# # 读取txt
# f = open("./test_questions.txt", "r", encoding='utf-8')

# keys = ["names", "lei", "sub_fund"]
# long_list = []
# long_text = {}
# LU = 'L'
# a = []
#
#
#
#
#
#
#
# for line in f.readlines()[10:25]:
#     curLine = line.strip().split('. ')
#     if curLine[0].isdigit() == True:
#         a = []
#         long_list.append(curLine)
#         long_list.append(a)
#     elif curLine[0][0].lower() == LU.lower():
#         a.append(curLine[0])
#     else:
#         long_list.append(curLine)
#
#
# a.clear()
# sub_fundd = []
#
#
# def sub_fund(long_list):
#     for i in range(len(long_list)):
#         if i < 2:
#             a.append(long_list[i][0])
#         elif long_list[i][0].isdigit() == True:
#             c = {"title": long_list[i][1]}
#             sub_fundd.append(c)
#         else :
#             d = {"isin": long_list[i]}
#             sub_fundd.append(d)
#         if i == (len(long_list) - 1):
#             a.append(sub_fundd)
#     return a
#
#
# print(long_list)
# list1 = sub_fund(long_list)
# print(list1[2])
# long_text = dict(zip(keys, list1))
# print(long_text.get("sub_fundd"))
# print('long_text:', long_text)
