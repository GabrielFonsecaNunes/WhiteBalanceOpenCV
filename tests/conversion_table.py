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
    row_values = str(text)\
                .replace("K", "")\
                .replace("deg", "")\
                .replace("  ", " ")\
                .split(" ")
    
    values = [valeu for valeu in row_values if valeu != ""]
    
    rgb_temp_dict["Temperature [K]"].append(values[0])
    rgb_temp_dict["CMF"].append(values[1])
    rgb_temp_dict["x"].append(values[2])
    rgb_temp_dict["y"].append(values[3])
    rgb_temp_dict["P"].append(values[4])
    rgb_temp_dict["R"].append(values[5])
    rgb_temp_dict["G"].append(values[6])
    rgb_temp_dict["B"].append(values[7])
    rgb_temp_dict["r"].append(values[8])
    rgb_temp_dict["g"].append(values[9])
    rgb_temp_dict["b"].append(values[10])
    rgb_temp_dict["#rgb"].append(values[11])
    

df = pd.DataFrame(data=rgb_temp_dict)

df.to_csv("./data/conversion_rgb_temp_full.csv", sep= ";", index= False, index_label="")

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
    row_values = str(text)\
                .replace("K", "")\
                .replace("deg", "")\
                .replace("  ", " ")\
                .split(" ")
    
    values = [valeu for valeu in row_values if valeu != ""]
    
    if int(values[0]) <= 15000:
        rgb_temp_dict["Temperature [K]"].append(values[0])
        rgb_temp_dict["CMF"].append(values[1])
        rgb_temp_dict["x"].append(values[2])
        rgb_temp_dict["y"].append(values[3])
        rgb_temp_dict["P"].append(values[4])
        rgb_temp_dict["R"].append(values[5])
        rgb_temp_dict["G"].append(values[6])
        rgb_temp_dict["B"].append(values[7])
        rgb_temp_dict["r"].append(values[8])
        rgb_temp_dict["g"].append(values[9])
        rgb_temp_dict["b"].append(values[10])
        rgb_temp_dict["#rgb"].append(values[11])

df = pd.DataFrame(data=rgb_temp_dict)
df.to_csv("./data/conversion_rgb_temp_15000.csv", sep= ";", index= False, index_label="")