# -*- coding: utf-8 -*-

import requests
import lxml.html

class TargetSelect:
    def __init__(self, name=None, select_term=None):
        self.name = name
        self.select_term = select_term

class TargetInfo:
    def __init__(self, name=None, info=None):
        self.name = name
        self.info = info

title = TargetSelect('product_title', 'h1#title > span#productTitle')
td = TargetSelect('area', 'tr#places_area__row > td.w2p_fw')
# asin = TargetSelect('ASIN', '')
# price = TargetSelect('price', 'tr#priceblock_ourprice_row > span#priceblock_ourprice')
price = TargetSelect('price', 'tr#priceblock_ourprice_row > td.a-span12 > span#priceblock_ourprice')


def scrape(html):
    targets = [title, price]
    # targets = [td, price]
    results = [TargetInfo(ele.name, None) for ele in targets ]
    tree = lxml.html.fromstring(html)
    # treestr = lxml.html.tostring(tree, pretty_print=True)
    # print(treestr)
    for i in range(len(targets) ):
        ele = tree.cssselect(targets[i].select_term )
        if ele:
            results[i].info = ele[0].text_content().strip()
        else:
            results[i].info = '*** failed ***'
        print(results[i].name + ': ' + results[i].info)
    return results

if __name__ == '__main__':
    seed_url = 'https://www.amazon.com/dp/B01J8PBEUM?th=1'
    # seed_url = 'http://example.webscraping.com/places/default/view/United-Kingdom-239'
    response = requests.get(seed_url)
    html = response.text 
    scrape(html)
