# long_text = """
# Variopartner SICAV
# 529900LPCSV88817QH61
# 1. TARENO GLOBAL WATER SOLUTIONS FUND
# LU2001709034
# LU2057889995
# LU2001709547
# 2. TARENO FIXED INCOME FUND
# LU1299722972
# 3. TARENO GLOBAL EQUITY FUND
# LU1299721909
# LU1299722113
# LU1299722030
# 4. MIV GLOBAL MEDTECH FUND
# LU0329630999
# LU0329630130
# """
# # 这一块和之前从网页提取相反，也就是将数据重新封装
# list_dic = []
# dic = {}
# for i in range(1, len(long_text.split('.'))):
#     print(long_text.split('.')[i])
#     dic1 = {}
#     list_isin = []
#     for j in range(1, len(long_text.split('.')[i].split('\n')) - 1):
#         dic1['title'] = long_text.split('.')[i].split('\n')[0]
#         list_isin.append(long_text.split('.')[i].split('\n')[j])
#     dic1['isin'] = list_isin
#     list_dic.append(dic1)
#     dic['name'] = long_text.split('.')[0].split('\n')[1]
#     dic['lei'] = long_text.split('.')[0].split('\n')[2]
#     dic['sub_fund'] = list_dic
#
# print(dic)

# 本来直接从txt中用用对应提取再封装，也能遍历。

# coding: utf8
import numpy as np

# 读取txt
f = open("./test_questions.txt", "r", encoding='utf-8')

keys = ["names", "lei", "sub_fund"]
long_list = []
long_text = {}
a = []

for line in f.readlines()[10:25]:
    inline = line.strip().split('.')
    if len(inline) == 2:
        long_list.append(a)
        a = [inline[1]]
    else:
        a.append(inline[0])

long_list.append(a)
values = long_list[0]
sub_fundd = []


def sub_fund(long_list):
    for i in range(1, len(long_list)):
        isin = []
        dic = {"title": long_list[i][0]}
        sub_fundd.append(dic)
        for j in range(1, len(long_list[i])):
            isin.append(long_list[i][j])
        dic = {"isin": isin}
        sub_fundd.append(dic)
    return sub_fundd


values.append(sub_fund(long_list))

long_text = dict(zip(keys, values))
# print(long_text.get("sub_fundd"))
print('long_text:', long_text)
