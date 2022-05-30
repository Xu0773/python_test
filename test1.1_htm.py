import urllib.request

#从url中提取到
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


def saveHtml(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    with open(file_name.replace('/', '_') + ".html", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)


# 保存到指定文件
aurl = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4"
html = getHtml(aurl)
saveHtml("D:\\Learning\\Data-processing\\test_5_30\\html\\COVID_19_data", html)

print("下载成功")
