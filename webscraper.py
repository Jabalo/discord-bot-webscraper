import requests
from bs4 import BeautifulSoup

def check_stock():
    URL = 'https://www.apple.com/ca/shop/product/FUHP2/refurbished-133-inch-macbook-pro-14ghz-quad-core-intel-core-i5-with-retina-display-space-grey?fnode=72ed490a40f8dd168bb12c866c4a9d052f2e9fb2d065d07d80ca6dd0e97b2e65e96bca6e5f397008b1de5e3e20b009fa7cdf09074121b01b66df93f57b6b44b8ad2765f0d1c16b77607174a0b4f41d5f'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='product-details-form')

    results_str = str(results)
    out_of_stock = 'Out of stock' in results_str

    print(out_of_stock)
    return out_of_stock