from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from datetime import datetime
import pandas as pd

file = open('./html/COVID_19_data.html', 'rb')
html = file.read()
soup = BeautifulSoup(html, 'html.parser')

# print(soup.head)
# print(soup.find('script', {'id': 'captain-config'}))

# 找最近的待想要找数据的块，定位
items = soup.find('script', {'type': 'application/json'})
# print(items)

# 找到对应的块后，将格式转为json开始提取数据
s = items.text.encode('utf-8').decode('unicode_escape')
json1 = json.loads(s, strict=False)

# 逐个拆开对应的字典或者列表
# print(json1)
# print(json1.keys())
# print(json1['component'])
# print(json1['component'][0])
# print(json1['component'][0].keys())
# print(json1['component'][0]['caseList'])

# 找到了'component'国内病例'caseOutsideList'国外病例对应的字典，以国内病例为例单个提取需要的数据
data = []
for i in range(len(json1['component'][0]['caseList'])):
    for j in range(len(json1['component'][0]['caseList'][i]['subList'])):
        dic = {'city': json1['component'][0]['caseList'][i]['subList'][j]['city'],
               'confirmedRelative': json1['component'][0]['caseList'][i]['subList'][j]['confirmedRelative'],
               'curConfirm': json1['component'][0]['caseList'][i]['subList'][j]['curConfirm'],
               'confirmed': json1['component'][0]['caseList'][i]['subList'][j]['confirmed'],
               'crued': json1['component'][0]['caseList'][i]['subList'][j]['crued'],
               'died': json1['component'][0]['caseList'][i]['subList'][j]['died']}
        data.append(dic)
data_df = pd.DataFrame(data)
data_df = data_df[data_df['city'] != '境外输入']
data_df = data_df[data_df['city'] != '待确认']
data_df.to_csv('data_' + str(datetime.now().timestamp()) + '.csv', index=False)
print(data_df)
