#import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
import requests
import pandas as pd


# def init_browser():
#     # @NOTE: Replace the path with your actual path to the chromedriver
#     executable_path = {'executable_path': '/Users/emmapang/code/chromedriver'}
#     browser = Browser('chrome', **executable_path, headless=False)


def scrape():

    executable_path = {'executable_path': '/Users/emmapang/code/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Mars News
    mars_news_url = 'https://mars.nasa.gov/news'
    browser.visit(mars_news_url)
    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    article_title = soup.find('div', class_='content_title').text
    article_body = soup.find('div', class_='article_teaser_body').text

    # Space images
    mars_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_img_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')

    html_2 = browser.html
    soup_2 = BeautifulSoup(html_2, 'html.parser')

    #print(soup_2)
    img_url = soup_2.find('img', class_='main_image').get('src')

    featured_image_url = f"https://www.jpl.nasa.gov{img_url}"

    mars_data = {
        "article_title": article_title,
        "article_body": article_body,
        "featured_image_url": featured_image_url


    }

    browser.quit()

    return mars_data