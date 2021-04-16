#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

from pprint import pprint

import csv

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://lichess.org/coach/en-GB/review")

# Uncomment to parse full list
scroll(driver, 5)

coaches = driver.find_elements_by_css_selector(".coach-widget")

coaches_parsed = []

for coach in coaches:
    c = {}
    try:
        name = coach.find_element_by_css_selector(".coach-name").text
        print(name)
        c['Name'] = name
        c['Country'] = coach.find_element_by_css_selector(".country").text
        c['Rate'] = coach.find_element_by_css_selector(".rate td").text
        c['Rating'] = coach.find_element_by_css_selector(".rating td").text.split()[1]
        c['Link'] = coach.find_element_by_css_selector(".overlay").get_attribute("href")
    except Exception as e:
        continue
#        print("Oops!", e.__class__, "occurred.")
    coaches_parsed.append(c)

with open('coaches.csv', mode='w') as csv_file:
    fieldnames = ['Name','Country','Rate','Rating','Link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for coach in coaches_parsed:
        writer.writerow(coach)

driver.quit()
