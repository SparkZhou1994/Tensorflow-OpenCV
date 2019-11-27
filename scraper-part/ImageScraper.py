# 8-2
import urllib
from bs4 import BeautifulSoup
# load url
html = urllib.request.urlopen('https://www.cnblogs.com/ybjourney/p/4702562.html')
# parse url
soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
# img
images = soup.findAll('img')
print(images)
imageName = 0
for image in images:
    link = image.get('src')
    print('link=',link)
    link = 'http:' + link
    fileFormat = link[-3:]
    if fileFormat == 'png' or fileFormat == 'jpg':
        fileSavePath = 'E:/'+ str(imageName)+'.jpg'
        imageName = imageName + 1
        urllib.request.urlretrieve(link,fileSavePath)