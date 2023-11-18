# Auto detect text files and perform LF normalization
* text=auto
from bs4 import BeautifulSoup
import requests

def scrape_zales_sale(base_url, num_pages):
    for page_num in range(1, num_pages + 1):
        url = f"{base_url}&loadMore={page_num}"

        # Make a request to the URL
        page_to_scrape = requests.get(url)

        if page_to_scrape.status_code == 200:
            soup = BeautifulSoup(page_to_scrape.text, "html.parser")

            productnames = soup.find_all("div", attrs={"class": "name product-tile-description"})
            prices = soup.find_all("div", attrs={"class": "price groupby-red-nowprice-font"})
            originalprices = soup.find_all("div", attrs={"class": "original-price"})

            for productname, price, originalprice in zip(productnames, prices, originalprices):
                print(productname.text.strip() + " - " + price.text.strip() + " - " + originalprice.text.strip())

        else:
            print(f"Failed to retrieve page {page_num}. Status code: {page_to_scrape.status_code}")

# Example usage
base_url = 'https://www.zales.com/sale-jewelry/c/011102101?icid=DEALS_LP:ALL_SALE'
num_pages = 225  # Change this to the number of pages you want to scrape

scrape_zales_sale(base_url, num_pages)
