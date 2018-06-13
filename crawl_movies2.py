# -*- coding: utf-8 -*-
import time
import requests
from lxml import etree


def get_html_text(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except:
        return ""


def parse_and_asve(url):
    html = get_html_text(url)
    selector = etree.HTML(html)
    infos = selector.xpath('//ul[@class="list-unstyled vod-item-img ff-img-215"]//li')
    for info in infos:
        try:
            movie_name = info.xpath('.//p[@class="image"]//img/@alt')[0]
            movie_img = info.xpath('.//p[@class="image"]//img/@data-original')[0]
            movie_url = 'http://nlook1.cn' + info.xpath('.//p[@class="image"]/a/@href')[0]
        except:
            print("")
        print(movie_name,movie_img,movie_url)
        time.sleep(1)
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write('{},,{},{}\n'.format(movie_name, movie_img, movie_url))


def main():
    url = 'http://nlook1.cn/index.php?s=/vod-type-id-1-type--area--year--star--state--order-addtime-p-{}.html'
    parse_and_asve(url)
    urls = ['http://nlook1.cn/index.php?s=/vod-type-id-1-type--area--year--star--state--order-addtime-p-{}.html'.format(str(i)) for i in range(2, 99)]
    for a_url in urls:
        parse_and_asve(a_url)
        print(a_url)


main()
