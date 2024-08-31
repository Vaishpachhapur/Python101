'''Web Scraper: Utilize libraries like Beautiful Soup or Scrapy to
extract data from websites. You can use our ShadowFox website
as a practice platform for data extraction.
'''
import requests
from bs4 import BeautifulSoup
import csv
def scrape_shadowfox(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='item') 
    scraped_data = []
    
    for item in items:
        try:
            title = item.find('h2', class_='title').text.strip() 
            price = item.find('span', class_='price').text.strip()  
            scraped_data.append([title, price])
        except AttributeError:
            print("An attribute error occurred while extracting item data.")
            continue
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price'])
        writer.writerows(scraped_data)
    
    print("Data scraping complete. Saved to 'scraped_data.csv'.")
url = 'https://www.shadowfox.in/' 
scrape_shadowfox(url)
