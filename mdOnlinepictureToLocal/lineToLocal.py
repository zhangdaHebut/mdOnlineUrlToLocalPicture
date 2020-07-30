import re
import urllib.request
import requests
import os

def download_img(img_url,img_name,file_name):
    if(not os.path.exists(file_name)):
        os.makedirs(file_name)

    file_name = file_name + img_name
    r = requests.get(img_url, { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'})
    if r.status_code == 200:
        open(file_name, 'wb').write(r.content)  # 将内容写入图片
        del  r
        return img_name
    del r
    return False


if __name__ == '__main__':
    print("请输入需要转换的.md文档的地址",'类似于：',r'C:/aaa/bbb/su.md')

    fileFullPath = input('地址为:')
    fileFullPath.replace('\\','/')
    baseName,dirName = os.path.split(fileFullPath)
    filename, extension = os.path.splitext(dirName)

    with open(fileFullPath ,encoding="UTF-8") as f:
        mdstr = f.read()
        pattern = re.compile(r'(?:!\[(.*?)\]\((.*?)\))')
        urldetails = pattern.findall(mdstr)

    for urldetail in urldetails:
        img_url = urldetail[1]
        img_name =img_url[-10:]
        file_name = baseName + '/assets/'
        downlod_result = download_img(img_url=img_url,img_name=img_name,file_name=file_name)
        mdstr.replace(img_url,'assets/'+downlod_result)
        print("download  "+img_url+"------"+"suceess")
    with open(os.path.join(baseName,filename+"_new"+extension) ,'w+') as f:
        f.write(mdstr)

