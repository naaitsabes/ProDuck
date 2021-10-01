import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

producten_lcdswaap = []

for page in range(1, 1):
    url = f"https://www.bol.com/nl/nl/w/alle-artikelen-lcdswaap-b-v/1541247/?page={page}"
    response = requests.get(f"{url}")
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    body = parser.body
    producten = body.find_all(class_="product-item--row js_item_root ")
    producten_lcdswaap.extend(producten)

# # productnaam = producten_lcdswaap[0].find(class_="product-title--inline").a.getText()

# productlijst = []

# for item in producten_lcdswaap:
#     product = item.find(class_="product-title--inline").a.getText()
#     productlijst.append([product])
    
# # print(productlijst[:1])
    
print(len(producten_lcdswaap))

# print(productnaam)