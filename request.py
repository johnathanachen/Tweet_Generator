import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver')
url = u'https://twitter.com/realDonaldTrump'

browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(700):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

tweets = browser.find_elements_by_class_name('tweet-text')

f = open("real_tweets.txt","a+")
for tweet in tweets:
    f.write("\n" + tweet.text + "\n")
