#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[24]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[25]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[26]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[27]:


slide_elem.find('div', class_='content_title')


# In[28]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[29]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[30]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[31]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[32]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[33]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[34]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[35]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[36]:


df.to_html()


# In[37]:


## browser.quit()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 

# ### Hemispheres

# In[45]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[49]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
results = browser.find_by_css('h3')
# print([result.value for result in results])

for result in range (len(results[:-1])):
    
    browser.find_by_css('h3')[result].click()
    
    full_res_elem = browser.find_by_text('Sample')
    img_url=full_res_elem["href"]
    
    title = browser.find_by_css("h2.title").text
    print(img_url)
    print(title)
    hemispheres = {
        'img_url' : img_url,
        'title' : title
    
    }

    hemisphere_image_urls.append(hemispheres)

    browser.back()


# In[50]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[22]:


# 5. Quit the browser
browser.quit()


# In[ ]:




