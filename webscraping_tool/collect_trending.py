import requests
import bs4
import argparse
import json
from pathlib import Path

def get_montreal_gazette_html_page():

    # No need for a cashe because the main page updates the trending articles all the time

    url = 'https://montrealgazette.com/category/news/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    data = requests.get(url, headers=headers)

    return data.text

def get_all_trending_links(gazette_main_page):

    prefix = 'https://montrealgazette.com'

    links_list = []

    soup = bs4.BeautifulSoup(gazette_main_page, 'html.parser')

    trending_div = soup.find('div', class_="col-xs-12 top-trending")

    for link in trending_div.find_all('a', class_='article-card__link'):
            links_list.append(prefix + (link.get('href')))
    
    return links_list

def get_trending_pages_html_data(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    cache_dir = Path('./cache')

    fpath = cache_dir / (url.replace('/', '_') + '.html')

    # Path doesn't exist in cache
    if not fpath.exists():

        data = requests.get(url, headers=headers)
        
        with open(fpath, 'w') as f:
            f.write(data.text)


    with open(fpath, 'r') as f:
         return f.read()
    

def fetch_info(html_page):
     
     info = []
     
     soup = bs4.BeautifulSoup(html_page, 'html.parser')

     header_div = soup.find('div', 'article-header__detail__texts')

     title = header_div.find('h1').get_text()
     info.append(title)

     publication_date = header_div.find('span', class_='published-date__since').get_text()
     info.append(publication_date)

     author = header_div.find('span', class_='published-by__author').get_text()
     info.append(author)

     blurb = header_div.find('p', class_='article-subtitle').get_text()
     info.append(blurb)

     return info




   



def main():

    Parser = argparse.ArgumentParser()

    Parser.add_argument("-o", "--output", help="Specify the json output file")

    args = Parser.parse_args()

    gazette_main_page = get_montreal_gazette_html_page()

    trending_links = get_all_trending_links(gazette_main_page)

    json_list = []

    for link in trending_links:
         
         html_page = get_trending_pages_html_data(link)

         info = fetch_info(html_page)

         json_data = {
              "title": info[0],
              "publication_date": info[1],
              "author": info[2],
              "blurb": info[3]
         }

         json_list.append(json_data)

    with open(args.output, 'w') as f:
        json.dump(json_list, f)
              


if __name__ == '__main__':
    main()