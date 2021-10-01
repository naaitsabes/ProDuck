import html
from autoscraper import AutoScraper
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

page = 1
while page != 2:

        # url = f"https://www.bol.com/nl/nl/w/alle-artikelen-lcdswaap-b-v/1541247/?page={page}"
        page = page + 1

        url = f"https://www.bol.com/nl/nl/w/alle-artikelen-lcdswaap-b-v/1541247/?page=1"

        wanted_list = ["Octopus knuffel - Mood knuffel - Roze - Blauw - Blij/Boos knuffel - Omkeerbaar - Emotie knuffel"]

        scraper = AutoScraper()

        # Here we can also pass html content via the html parameter instead of the url (html=html_content)
        result = scraper.build(url, wanted_list)


        print(result)
