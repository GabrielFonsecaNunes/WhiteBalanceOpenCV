import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "http://www.vendian.org/mncharity/dir3/blackbody/UnstableURLs/bbr_color.html"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
spans = soup.find_all('span')

def process_values(text):
    """
    Process raw text and split it into a list of cleaned values.

    Args:
        text (str): Raw text to be processed.

    Returns:
        list: List of cleaned values.
    """
    values = text.replace("K", "").replace("deg", "").replace("  ", " ").split(" ")
    return [value for value in values if value]

def extract_data(values):
    """
    Create a dictionary of extracted data from cleaned values.

    Args:
        values (list): List of cleaned values.

    Returns:
        dict: Extracted data in dictionary form.
    """
    return {
        "Temperature [K]": values[0],
        "CMF": values[1],
        "x": values[2],
        "y": values[3],
        "P": values[4],
        "R": values[5],
        "G": values[6],
        "B": values[7],
        "r": values[8],
        "g": values[9],
        "b": values[10],
        "#rgb": values[11]
    }

def process_spans(spans, filter_threshold=None):
    """
    Process a list of spans and extract data based on filtering criteria.

    Args:
        spans (list): List of BeautifulSoup span elements.
        filter_threshold (int, optional): Filtering threshold for temperature. Defaults to None.

    Returns:
        pd.DataFrame: Processed data in DataFrame form.
    """
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
        values = process_values(text)

        if filter_threshold is None or int(values[0]) <= filter_threshold:
            data = extract_data(values)
            for key, value in data.items():
                rgb_temp_dict[key].append(value)

    return pd.DataFrame(data=rgb_temp_dict)

# df_full = process_spans(spans)
# df_full.to_csv("./data/conversion_rgb_temp_full.csv", sep=";", index=False, index_label="")

df_filtered = process_spans(spans, filter_threshold=6600)
df_filtered.to_csv("./data/conversion_rgb_temp_6600.csv", sep=";", index=False, index_label="")

# df_filtered = process_spans(spans, filter_threshold=15000)
# df_filtered.to_csv("./data/conversion_rgb_temp_6600_15000.csv", sep=";", index=False, index_label="")

# df_filtered = process_spans(spans, filter_threshold=15000)
# df_filtered.to_csv("./data/conversion_rgb_temp_15000.csv", sep=";", index=False, index_label="")