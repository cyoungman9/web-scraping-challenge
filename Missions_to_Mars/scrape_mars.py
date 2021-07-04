
def scrape():
  from bs4 import BeautifulSoup
  from splinter import Browser
  import requests
  import pandas as pd
  import re
  # import pymongo
  import time 
  from webdriver_manager.chrome import ChromeDriverManager
  mars_dict = {}

  executable_path = {'executable_path': ChromeDriverManager().install()}
  browser = Browser('chrome', **executable_path, headless=False)

  url = "https://redplanetscience.com/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  news_title = soup.title.text

  mars_dict["news_title"]=news_title

  paragraphs = soup.find_all('p')
  for paragraph in paragraphs:
#     
    news_p = paragraph.text
  news_p  

  mars_dict["news_p"]=news_p

  url = 'https://spaceimages-mars.com/'
  browser.visit(url) 
  featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'

  mars_dict["featured_image_url"]=featured_image_url

  mars_url = 'http://space-facts.com/mars/'
  tables = pd.read_html(mars_url)
  df = tables[0]
  df.head(10)
  html_table = df.to_html()
  
  mars_dict["html_table"]=html_table

  url = 'https://marshemispheres.com/'
  browser.visit(url)
  hemisphere_urls = []
  html =  browser.html
  img_soup = BeautifulSoup(html, "html.parser")

  hemisphere_image_urls = []
  img_item = img_soup.find_all('div', class_ = 'item')
  img_item

  for item in img_item:
    
    div = item.find('div', class_='description')
    href=div.a['href']
    
    hemi_url = (url + href)
    
    name = div.find('h3').text
    
    hem_name = name.rsplit(' ', 1)[0]
     
    browser.visit(hemi_url)
        
    html = browser.html
        
    img_soup = BeautifulSoup(html, 'html.parser')
        
    img_tag = img_soup.find('img', class_='wide-image')
            
    img = img_tag['src']
        
    img_url = (url + img)
        
    hemisphere_dict = {}
    hemisphere_dict['title'] = hem_name
    hemisphere_dict['img_url'] = img_url
    hemisphere_image_urls.append(hemisphere_dict)
  
    mars_dict["img_url"]=img_url

    # mars_dict["hemisphere_dict"]=hemisphere_dict

    browser.quit()

    return mars_dict