#import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
import requests
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': '/Users/emmapang/code/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

    mars_news_url = 'https://mars.nasa.gov/news'
    browser.visit(mars_news_url)
    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    article_title = soup.find('div', class_='content_title').text
    article_body = soup.find('div', class_='article_teaser_body').text

    mars_data = {
        "article_title": article_title,
        "article_body": article_body,

    }

    browser.quit()

    return mars_data