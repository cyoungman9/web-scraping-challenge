from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
  executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

hemisphere_img_url = []


url = 'https://marshemispheres.com/'
browser.visit(url)


html = browser.html
soup = BeautifulSoup(html, 'html.parser')





mars_data = {}



browser.quit()

return mars_data