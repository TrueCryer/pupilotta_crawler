# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from xml.etree import ElementTree as ET
from urllib import request

import pandas as pd

def kolyasky():
    rq = request.urlopen('http://xn--h1adadot1h.xn--p1ai/prices.xml')
    tree = ET.fromstring(rq.read())
    items = tree.findall('.//item')

    NAME = []
    BRAND = []
    ARTIKUL = []
    PRICE1 = []
    REST = []
    IMAGE = []

    for i in items:
        NAME.append(i.find('./NAME').text)
        BRAND.append(i.find('./BRAND').text)
        ARTIKUL.append(i.find('./ARTIKUL').text)
        PRICE1.append(i.find('./PRICE1').text)
        REST.append(i.find('./REST').text)
        IMAGE.append(i.find('./IMAGE').text)

    df = pd.DataFrame([
        pd.Series(NAME),
        pd.Series(BRAND),
        pd.Series(ARTIKUL),
        pd.Series(PRICE1),
        pd.Series(REST),
        pd.Series(IMAGE)
    ], headers=['Наименование', 'Бренд', 'Артикул',
                'Цена', 'Остаток', 'Картинка'])