from lxml import html
import requests
import sys
import json
from time import sleep
from bs4 import BeautifulSoup
import _thread


def save(item):
    with open('itemurl.json', 'a', encoding='utf-8') as f:
        json.dump(item, f)
        f.close()
        #data = json.load(f)
        #data.update(json.dumps(item))

def name_exract(html):
    page = BeautifulSoup(html, 'html.parser')
    mid  = page.findAll("td", {"style":"line-height:15px"})
    name = mid[1].strong.text
    return name


def data(data_url):
    #print(data_url)
    page = requests.get('https://www.car.gr'+data_url)
    tree = html.fromstring(page.content)
    path = tree.xpath('//*[@itemprop="telephone"]/text()')
    tree = html.fromstring(page.text)
    name = "empty"
    try:
        name = name_exract(page.text)
    except Exception as e:
        pass
    if len(path) == 0:
        #print('empty')
        return False
    else:
        data = "{Name: "+name+",Telephone:"+path[0].strip(' \t\n\r')+",url:"+data_url+"},"
        save(data)
        sleep(0)
        print(data)
        #print(list(name))
        return True




def inside_url(url):
    url_start = 'https://www.car.gr'+url
    page = requests.get(url_start)
    tree = html.fromstring(page.content)
    path = tree.xpath('//*[contains(@class, "vehicle list-group-item clsfd_list_row")]/@href')
    save(path)
    # print(list(path))
    index=0
    length = len(path)
    print(str(length) + url_start)
    while index<len(path):
        #print('suburl=> '+ path[index])
        type = data(path[index])
        #url_start = 'https://www.car.gr'+path[0]
        sleep(0.1)
        index =  index + 1


def main(st, i):
    print("thread: %s start" % i)
    url_start = 'https://www.car.gr/classifieds/cars/?condition=%CE%9A%CE%B1%CE%B9%CE%BD%CE%BF%CF%8D%CF%81%CE%B9%CE%BF&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&offer_type=sale&pg='+st
    while True:
        page = requests.get(url_start)
        tree = html.fromstring(page.content)
        path = tree.xpath('//*[contains(@class,"next")]/@href')
        inside_url(path[0])
        url_start = 'https://www.car.gr'+path[0]


if __name__ == '__main__':

    # main("1")
    id = 1
    for i in range(int(sys.argv[1])):
        try:
            st= str(id)
            _thread.start_new_thread( main, (st,str(i)) )
            id=id+50
            sleep(1)
        except Exception as e:
            print("Error: unable to start thread")


    while True:
        sleep(12)
        print("a")
