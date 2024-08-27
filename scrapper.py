from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import math
import pandas as pd


offersList=[]

def findNumberOfOffers(soup):
    offersElement = soup.find(class_='MuiTab-iconWrapper css-1604j7q')
    offers = offersElement.text
    words = offers.split()
    words.pop()
    offers_num = int(words[0])
    return offers_num


def scrapOffer(soup):
    offers = soup.find_all(class_='MuiBox-root css-sslmpj')

    for i in range(len(offers)):
        offerInfoList = []

        title = offers[i].find_all(class_='css-1gehlh0')
        offerInfoList.append(title[0].text)

        salary = offers[i].find_all(class_='MuiBox-root css-18ypp16')
        offerInfoList.append(salary[0].text)

        informations = offers[i].find_all(class_='MuiBox-root css-1qruno6')
        for i in range(len(informations)):
            if(informations[i].text == 'Fully remote'):
                continue
            else:
                offerInfoList.append(informations[i].text)

        offersList.append(offerInfoList)


def writeToTxt():
    with open('jobs.txt', 'w', encoding='utf-8') as file:
        for offer in offersList:
            file.write(','.join(offer) + '\n')
        file.flush()

def writeToExcel():
    #There are maximum 3 skills required in each offer
    headers = ['Position', 'Salary', 'Status', 'Skill 1', 'Skill 2', 'Skill 3']
    list_of_dicts = [dict(zip(headers, item)) for item in offersList]

    df = pd.DataFrame(list_of_dicts)
    df.to_excel("job_offers.xlsx", index=False)


def run_scrapper(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    time.sleep(3)

    soup = bs(driver.page_source, features="html.parser")
    offers = findNumberOfOffers(soup)

    # setting the number of scrolls the script must perform to collect all offers.
    # with the current settings the script collects all offers and does not duplicate offers.
    iterations = math.floor(offers / 26)
    scrollValue = 0

    for i in range(iterations):
        scrapOffer(soup)
        time.sleep(1)
        if i == iterations - 1:
            scrollValue += 800
        else:
            scrollValue += 2340
            driver.execute_script(f"window.scrollTo(0, {scrollValue});")
        
        time.sleep(2.4)

        soup = bs(driver.page_source, features="html.parser")

if __name__ == "__main__":
    url = 'https://justjoin.it/poznan'
    run_scrapper(url)
    writeToTxt()
    writeToExcel()

