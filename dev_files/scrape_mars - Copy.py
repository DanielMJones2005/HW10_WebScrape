#!/usr/bin/env python
# coding: utf-8

# ## Scrape Function

# In[ ]:


# Convert your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape 


# In[8]:


def scrape():
    # Dependencies
    from splinter import Browser
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import pymongo
    import time
    import ctypes  # An included library with Python install.
    
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    
    mars_data_dict = {}
    
    ## (1) NASA Mars News
    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
    # Assign the text to variables that you can reference later.
       
    # URL of page to be scraped
    url_nz = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response_nz = requests.get(url_nz)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_nz = BeautifulSoup(response_nz.text, 'lxml')

    # Examine the results, then determine element that contains sought info
    #print(soup_nz.prettify())
    
    #time.sleep(2)
    
    # Find the latest News Title
    news_title = soup_nz.find("div", class_="content_title").a.text[1:-1]
    #print(news_title)
    
    # Find the latest News Paragraph Text
    news_p = soup_nz.find("div", class_="image_and_description_container").a.text[3:-7]
    #print(news_p)
    
    mars_data_dict["news_title"] = news_title
    mars_data_dict["news_p"] = news_p
        
        
    
    ## (2) JPL Mars Space Images - Featured Image
    # Use splinter to navigate the site and find the image url for the current Featured Mars Image 
    # and assign the url string to a variable called featured_image_url.
    # Make sure to find the image url to the full size .jpg image.
    # Make sure to save a complete url string for this image.
    
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_jpl)
    
    time.sleep(2)
    
    #dir(browser)
    
    browser.click_link_by_id('full_image')
    
    time.sleep(2)
    
    browser.click_link_by_partial_href("/spaceimages/details.")
    
    time.sleep(2)
    
    browser.click_link_by_partial_href("/spaceimages/images/largesize")
    
    time.sleep(2)
    
    featured_image_url = browser.url
    #print(featured_image_url)
    
    mars_data_dict["feat_img"] = featured_image_url
    
    browser.quit()
    
           
    
    ## (3) Mars Weather
    # Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page.
    # Save the tweet text for the weather report as a variable called mars_weather.
        
    # URL of page to be scraped
    url_tweet = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    response_tweet = requests.get(url_tweet)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_tweet = BeautifulSoup(response_tweet.text, 'lxml')

    # Examine the results, then determine element that contains sought info
    #print(soup_tweet.prettify())
    
    #time.sleep(2)
    
    # scrape the latest Mars weather tweet from the page
    tweets = soup_tweet.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    for tweet in tweets:
        find_text = tweet.text.find("InSight sol")
        if find_text == 0:
            mars_weather = tweet.text
            #print(mars_weather)
            break
    
    mars_data_dict["weather"] = mars_weather
    
    
    
    ## (4) Mars Facts
    # URL of page to be scraped
    url_mfacts = 'https://space-facts.com/mars/'

    # Retrieve page with the requests module
    response_mfacts = requests.get(url_mfacts)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_mfacts = BeautifulSoup(response_mfacts.text, 'lxml')

    # Examine the results, then determine element that contains sought info
    #print(soup_mfacts.prettify())
    
    #time.sleep(2)
    
    tables = pd.read_html(url_mfacts)[1]
    #tables
    
    mars_data_dict["mfacts"] = tables
    
    tables.to_html("../html/mars_facts.html")
    
    
    
    ## (5) Mars Hemispheres
    # Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
    # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # Save both the image url string for the full resolution hemisphere image, 
    #     and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the 
    #     keys img_url and title.
    # Append the dictionary with the image url string and the hemisphere title to a list. 
    #     This list will contain one dictionary for each hemisphere
    
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

    # URL of page to be scraped
    url_mhemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_mhemi)
    
    time.sleep(2)
    
    # Image 1
    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")
    
    time.sleep(2) 
    
    title1 = browser.title.split("|")[0]
    #print(title1)
    
    browser.click_link_by_text("Sample")
    
    time.sleep(2)
    
    img1_url = browser.windows[1].url
    #print(img1_url)
    
    time.sleep(2) 
    
    browser.windows[1].close()
    browser.back()
    
    hemi1_dict = {}
    hemi1_dict["title"] = title1
    hemi1_dict["img_url"] = img1_url
    #hemi1_dict
    
    # Image 2
    
    browser.click_link_by_partial_text("Schiaparelli Hemisphere Enhanced")
    
    time.sleep(2)
    
    title2 = browser.title.split("|")[0]
    #print(title2)
    
    browser.click_link_by_text("Sample")
    
    time.sleep(2)
    
    img2_url = browser.windows[1].url
    #print(img2_url)
    
    time.sleep(2)
    
    browser.windows[1].close()
    browser.back()
    
    hemi2_dict = {}
    hemi2_dict["title"] = title2
    hemi2_dict["img_url"] = img2_url
    #hemi2_dict
    
    # Image 3
    
    browser.click_link_by_partial_text("Syrtis Major Hemisphere Enhanced")
    
    time.sleep(2)
    
    title3 = browser.title.split("|")[0]
    #print(title3)
    
    browser.click_link_by_text("Sample")
    
    time.sleep(2)
    
    img3_url = browser.windows[1].url
    #print(img3_url)
    
    time.sleep(2)
    
    browser.windows[1].close()
    browser.back()
    
    hemi3_dict = {}
    hemi3_dict["title"] = title3
    hemi3_dict["img_url"] = img3_url
    #hemi3_dict
    
    # Image 4
    browser.click_link_by_partial_text("Valles Marineris Hemisphere Enhanced")
    
    time.sleep(2)
    
    title4 = browser.title.split("|")[0]
    #print(title4)
    
    browser.click_link_by_text("Sample")
    
    time.sleep(2)
    
    img4_url = browser.windows[1].url
    #print(img4_url)
    
    time.sleep(2)
    
    browser.windows[1].close()
    browser.back()
    
    hemi4_dict = {}
    hemi4_dict["title"] = title4
    hemi4_dict["img_url"] = img4_url
    #hemi4_dict
    
    hemisphere_image_urls = [hemi1_dict, hemi2_dict, hemi3_dict, hemi4_dict]
    #hemisphere_image_urls
    
    mars_data_dict["hemi_img"] = hemisphere_image_urls
    mars_data_dict  
    
    browser.quit()
    

    
    Mbox("Mission to Mars Completed", "Congratulations!!! You've mined Mars!", 1)   




