# Mission to Mars

![alt text](https://github.com/DanielMJones2005/HW10_WebScrape/blob/master/img/mission_to_mars.png)


## Files
* [Dev_Files](https://github.com/DanielMJones2005/HW10_WebScrape/tree/master/dev_files)
    * various files for development
    
* [html](https://github.com/DanielMJones2005/HW10_WebScrape/tree/master/html)
    * mars_facts.html
      * Python html export
      
* [img](https://github.com/DanielMJones2005/HW10_WebScrape/tree/master/img)
    * HW10_WebScrape.FeatureImg.jpg
    * HW10_WebScrape.Hemi.jpg
    * HW10_WebScrape.ScreenShot_whole_page.jpg
    * HW10_WebScrape.Top.jpg
    * final_app_part1.png
    * final_app_part2.png
    * mission_to_mars.png

* [static](https://github.com/DanielMJones2005/HW10_WebScrape/tree/master/static)
    * mission_to_mars.png
        * this folder is for Flask to access image
 
 * [templates](https://github.com/DanielMJones2005/HW10_WebScrape/tree/master/templates)
    * index.html
  
 * [.gitignore](https://github.com/DanielMJones2005/HW10_WebScrape/blob/master/.gitignore)
 * [app.py](https://github.com/DanielMJones2005/HW10_WebScrape/blob/master/app.py)
 * [mission_to_mars.ipynb](https://github.com/DanielMJones2005/HW10_WebScrape/blob/master/mission_to_mars.ipynb)
 * [scrape_mars.py](https://github.com/DanielMJones2005/HW10_WebScrape/blob/master/scrape_mars.py)

 ## Step 1 - Scraping
 - Completed initial scraping using
    - Jupyter Notebook
    - BeautifulSoup
    - Pandas and
    - Requests/Splinter
 - Created a Jupyter Notebook file called mission_to_mars.ipynb
    - Used this to complete all scraping and analysis tasks
    - NASA Mars News
 - Scraped the NASA Mars News Site and collected
    - latest News Title and 
    - Paragraph Text 
    - assigned the text to variables to reference later
        - news_title
        - news_p
 - JPL Mars Space Images - Featured Image
    - Visited the url for JPL Featured Space Image
        - https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    - Used splinter to navigate the site and 
        - found the image url for the current Featured Mars Image and 
        - assigned the url string to a variable called featured_image_url
        - found full size .jpg image
        - saved a complete url string for this image
 - Mars Weather
    - Visited the Mars Weather twitter account
        - https://twitter.com/marswxreport?lang=en
        - scraped the latest Mars weather tweet from the page
        - saved the tweet text for the weather report as a variable called mars_weather   
 - Mars Facts
    - Visited the Mars Facts webpage
        - https://space-facts.com/mars/
        - used Pandas to scrape the table containing facts about the planet
            - including Diameter, Mass, etc.
        - used Pandas to convert the data to a HTML table string
 - Mars Hemispheres
        - visit the USGS Astrogeology site here 
            - https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
        - obtained high resolution images for each of Mar's hemispheres
        - saved both the image url string for the full resolution hemisphere image and 
            - the Hemisphere title containing the hemisphere name. 
        - used a Python dictionary to store the data using the keys img_url and title
        - appended the dictionary with the image url string and the hemisphere title to a list
            - hemisphere_image_urls
        - list contained one dictionary for each hemisphere.
 
 ## Step 2 - MongoDB and Flask Application
   - used MongoDB with Flask template to create a new HTML page
        - that displayed all of the information that was scraped from the URLs above
   - converted Jupyter notebook into a Python script called scrape_mars.py 
        - with a function called scrape
            - that will execute scraping code from above and 
            - return one Python dictionary containing all of the scraped data

  - created a route called /scrape that 
        - imports the scrape_mars.py script and calls the scrape function
  - stored the return value in Mongo as a Python dictionary
  - created a root route / that 
        - queries the Mongo database and 
        - passes the mars data into an HTML template to display the data
  - created a template HTML file called index.html that 
        - takes the mars data dictionary and 
        - displays all of the data in the appropriate HTML elements. 
        
## Step 3 - Submission
  - Submit your work to BootCampSpot, create a new GitHub repository and upload the following:
        - The Jupyter Notebook containing the scraping code used (see above and github repo)
        - Screenshots of your final application (see below)
        - Submit the link to your new repository to BootCampSpot
 
 
 
 
 
 
 
        
    
    
    
    
    
    
    
    
