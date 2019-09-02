from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pymongo
import time
import ctypes  # An included library with Python install.

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():     
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    mars_data_dict = {}
    
    ## (1) NASA Mars News
    url_nz = 'https://mars.nasa.gov/news/'
    response_nz = requests.get(url_nz)
    soup_nz = BeautifulSoup(response_nz.text, 'lxml')
    
    # Find the latest News Title
    news_title = soup_nz.find("div", class_="content_title").a.text[1:-1]
    
    # Find the latest News Paragraph Text
    news_p = soup_nz.find("div", class_="image_and_description_container").a.text[3:-7]
    
    mars_data_dict["news_title"] = news_title
    mars_data_dict["news_p"] = news_p
        
        
    
    ## (2) JPL Mars Space Images - Featured Image
    browser = init_browser()

    url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_jpl)
    time.sleep(2)
     
    browser.click_link_by_id('full_image')
    time.sleep(2)
    
    browser.click_link_by_partial_href("/spaceimages/details.")
    time.sleep(2)
    
    browser.click_link_by_partial_href("/spaceimages/images/largesize")
    time.sleep(2)
    
    featured_image_url = browser.url
    mars_data_dict["feat_img"] = featured_image_url
    browser.quit()
    
           
    
    ## (3) Mars Weather
    url_tweet = 'https://twitter.com/marswxreport?lang=en'
    response_tweet = requests.get(url_tweet)
    soup_tweet = BeautifulSoup(response_tweet.text, 'lxml')
    
    # scrape the latest Mars weather tweet from the page
    tweets = soup_tweet.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    for tweet in tweets:
        find_text = tweet.text.find("InSight sol")
        if find_text == 0:
            mars_weather = tweet.text
            break

    mars_data_dict["weather"] = mars_weather
    
    
    
    ## (4) Mars Facts
    url_mfacts = 'https://space-facts.com/mars/'
    response_mfacts = requests.get(url_mfacts)
    soup_mfacts = BeautifulSoup(response_mfacts.text, 'lxml')
    tables = pd.read_html(url_mfacts)[1]
 
    mars_data_dict["mfacts"] = tables.to_html("mars_facts.html")
    ## mars_data_dict["mfacts"] = tables
    tables.to_html("../html/mars_facts.html")
    
    
    
    ## (5) Mars Hemispheres
    browser = init_browser()
    url_mhemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_mhemi)
    time.sleep(2)
    
    # Image 1
    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")
    time.sleep(2) 
    
    title1 = browser.title.split("|")[0]

    browser.click_link_by_text("Sample")
    time.sleep(2)
    
    img1_url = browser.windows[1].url
    time.sleep(2) 
    
    browser.windows[1].close()
    browser.back()
    
    hemi1_dict = {}
    hemi1_dict["title"] = title1
    hemi1_dict["img_url"] = img1_url
    
    # Image 2
    browser.click_link_by_partial_text("Schiaparelli Hemisphere Enhanced")
    time.sleep(2)
    
    title2 = browser.title.split("|")[0]
    
    browser.click_link_by_text("Sample")
    time.sleep(2)
    
    img2_url = browser.windows[1].url
    time.sleep(2)
    
    browser.windows[1].close()
    browser.back()
    
    hemi2_dict = {}
    hemi2_dict["title"] = title2
    hemi2_dict["img_url"] = img2_url
    
    # Image 3
    browser.click_link_by_partial_text("Syrtis Major Hemisphere Enhanced")
    time.sleep(2)
    
    title3 = browser.title.split("|")[0]
    
    browser.click_link_by_text("Sample")
    time.sleep(2)
    
    img3_url = browser.windows[1].url
    time.sleep(2)
    
    browser.windows[1].close()
    browser.back()
    
    hemi3_dict = {}
    hemi3_dict["title"] = title3
    hemi3_dict["img_url"] = img3_url
    
    # Image 4
    browser.click_link_by_partial_text("Valles Marineris Hemisphere Enhanced")
    time.sleep(2)
    
    title4 = browser.title.split("|")[0]
    
    browser.click_link_by_text("Sample")
    time.sleep(2)
    
    img4_url = browser.windows[1].url
    time.sleep(2)
    
    browser.windows[1].close()
    browser.back()
    
    hemi4_dict = {}
    hemi4_dict["title"] = title4
    hemi4_dict["img_url"] = img4_url
    
    hemisphere_image_urls = [hemi1_dict, hemi2_dict, hemi3_dict, hemi4_dict]
    
    mars_data_dict["hemi_img"] = hemisphere_image_urls
    mars_data_dict  
    
    browser.quit()
    
    Mbox("Mission to Mars Completed", "Congratulations!!! You've mined Mars!", 1)   

    return mars_data_dict

    




