import requests
from lxml import html
import json
from time import sleep
from bs4 import BeautifulSoup
import sys
import _thread
from selenium import webdriver

headers = {
    'Cookie':'nQ_visitId=7b75e1d9-1282-5e20-c66a-22d1edbf0897%3A1523879661893; csrftoken=GRL8qSAS4xF7pqmUvBNCTMM3ApiiZ2U5LXblv2nTbZGeZ3QFC1yy0OZgVH1CRHeE; anonymous_id=f4540d53-3340-4916-8234-7e06b51634ab; AWSELB=5719717106E49DAF1DD69CFBD855327522CF12026743027FBA6881582B2D36CEFB53E09F24C5236A10B3E687F78292D0648A8C37F0446F8D8E9EA979C84C3B1F72DD2CF5BF; _ga=GA1.2.2119647969.1523879386; _gid=GA1.2.204270660.1523879386; nQ_cookieId=75d0289e-9c60-8812-588b-f09b60dc367e; _gat_UA-35115110-1=1; nQ_visitId=7b75e1d9-1282-5e20-c66a-22d1edbf0897%3A1523879666611',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

def data(data_url):
    print(data_url)
    #print(data_url)
    try:
        page = requests.get(data_url, headers=headers)
        tree = html.fromstring(page.content)
        name = tree.xpath('//*[@id="list-page-description"]/h1/text()')
        tel = tree.xpath("//*[contains(@class, 'p-tel')]/text()")
        dat = "{Name: "+str(name[0]).strip(' \t\n\r')+",Telephone:"+str(tel[0]).strip(' \t\n\r')+",url:"+data_url+"},"
        print(dat)
        if dat:
            save(dat)
            print(dat)
        else:
            pass

    except Exception as e:
        pass


def inside_url(url):
    print(url)
    #url_start = 'https://www.11888.gr'+url
    page = requests.get(url,headers=headers)
    tree = html.fromstring(page.content)
    path = tree.xpath('//a/@href')
    print(list(path))
    #save(path)
    # print(list(path))
    index=0
    length = len(path)
    #print(str(length) + url_start)
    while index<len(path):
        print('suburl=> '+ path[index])
        type = data(path[index])
        sleep(0.1)
        index =  index + 1

def save(data):
    with open("site88url.json", 'a') as f:
        json.dump(data, f)
        f.write('\n')


#https://www.11888.gr/search/?query=%20%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%B5%CF%82
def query(word):
    print("query")
    path = requests.get(word)
    inside_url(word)


if __name__ == '__main__':
    #word = ["λογιστες"]
    #query("https://www.11888.gr/search/?query=%20%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%B5%CF%82")
    cities = ['Αναξαγόρας','Αναξήνωρ','Αναξίβιος','Αναξίλαος','Αναξίμανδρος','Αναξιμένης','Αναξίπολις','Ανάξιππος','Ανάργυρος','Αναστάσης','Αναστάσιος','Ανατόλιος','Ανδρέας','Ανδροκλής','Ανδρόνικος','Ανδρόφιλος','Ανέστης','Ανθέμιος','Άνθιμος','Αννίβας','Ανταίος','Αντίγονος','Αντίμαχος','Αντίνοος','Αντίπατρος','Αντρέας','Αντρίκος','Αντύπας','Αντωνάκης','Αντώνης','Αντώνιος','Ανύσιος','Αξιώτης','Απελλής','Απολλόδωρος','Απόλλων','Αποστόλης','Απόστολος','Αργύρης','Αργύριος','Άρης','Αρθούρος','Αρίσταρχος','Αριστέας','Αριστείδης','Αρίστιππος','Αριστίων','Αριστόβουλος','Αριστογείτων','Αριστογένης','Αριστόδημος','Αριστόδικος','Αριστόδουλος','Αριστοκλής','Αριστόμαχος','Αριστομένης','Αριστόνικος','Αριστόνους','Αρίστος','Αριστοφάνης','Αρίων','Αρκάδιος','Αρκτούρος','Αρμάνδος','Αρμόδιος','Αρριανός','Αρσένης','Αρσένιος']

    
    chrome_driver= r"chromedriver.exe"
    browser =  webdriver.Chrome(executable_path=chrome_driver)

    for key in cities:
        browser.get("https://www.11888.gr/search/?query="+key+"&")
        dat = browser.find_elements_by_tag_name('a')
        for i in dat:
            a = str(i.get_attribute("href"))
            print(i.get_attribute("href"))
            data(a)