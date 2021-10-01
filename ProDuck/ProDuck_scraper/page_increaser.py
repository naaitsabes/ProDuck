import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

page = 1
while page != 6:
      url = f"https://www.bookdepository.com/bestsellers?page={page}"
      print(url)
      page = page + 1