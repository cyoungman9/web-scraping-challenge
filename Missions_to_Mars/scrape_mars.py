
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

  paragraphs = soup.find_all('p')
  for paragraph in paragraphs:
#     
    news_p = paragraph.text
  news_p  

  mars_dict["news_title"]=news_title
  mars_dict["news_p"]=news_p

  featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'

  mars_dict["featured_image_url"]=featured_image_url

  url = 'https://marshemispheres.com/'
  browser.visit(url)
  hemisphere_urls = []
  html =  browser.html
  img_soup = BeautifulSoup(html, "html.parser")

  # mars_dict["hemisphere_urls"]=

  browser.quit()

  return mars_dict