import pandas as pd
import requests
from bs4 import BeautifulSoup
from IPython.display import display

url = "http://www.vendian.org/mncharity/dir3/blackbody/UnstableURLs/bbr_color.html"


response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
spans = soup.find_all('span')

rgb_temp_dict = {
    "Temperature [K]": [], 
    "CMF": [], 
    "x": [], 
    "y": [], 
    "P": [], 
    "R": [], 
    "G": [], 
    "B": [], 
    "r": [], 
    "g": [], 
    "b": [], 
    "#rgb": []
}

for span in spans:
    text = span.get_text(strip=True)
    values = str(text)\
                .replace("K", "")\
                .replace("deg", "")\
                .split("  ")
    
    

df = pd.DataFrame(data=rgb_temp_dict)

df.to_csv("./data/conversion_rgb_temp.csv", sep= ";", index= False, index_label="")

import pandas as pd

df = pd.read_csv("./data/conversion_rgb_temp.csv", sep=";")


display(df.head().to_html) # type: ignore