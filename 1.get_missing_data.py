from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


#Test with 1 FIFA World Cup edition


# Download ChromeDriver -> https://chromedriver.chromium.org/downloads
path = 'D/Desktop/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)


# Test with 1 FIFA World Cup Edition (1982)

web = 'https://en.wikipedia.org/wiki/1982_FIFA_World_Cup'

driver.get(web)


matches = driver.find_elements(by='xpath', value='//td[@align="right"]/.. | //td[@style="text-align:right;"]/..')

home=[]
score=[]
away=[]

for match in matches:
    home.append(match.find_elements(by='xpath', value='./td[1]'))
    score.append(match.find_elements(by='xpath', value='./td[2]'))
    away.append(match.find_elements(by='xpath', value='./td[3]'))
    
dict_football={'home': home,'score':score,'away':away}
df_football = pd.DataFrame(dict_football)
df_football['year'] = 1982
time.sleep(2)

driver.quit()

df_football.to_csv('data/fifa_worldcup_missing_data.csv', index=False)


# Applied to all editions (from 1930 to 2018)

path = 'D/Desktop/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

years = [
    1930,1934,1938,1950,1958,1962,1966,1970,1974,1978,
    1982,1986,1990,1994,1998,2002,2006,2010,2014,2018
]

def get_missing_data(year):
    web = 'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    driver.get(web)

    matches = driver.find_elements(by='xpath', value='//td[@align="right"]/.. | //td[@style="text-align:right;"]/..')

    home=[]
    score=[]
    away=[]

    for match in matches:
        home.append(match.find_elements(by='xpath', value='./td[1]').text)
        score.append(match.find_elements(by='xpath', value='./td[2]').text)
        away.append(match.find_elements(by='xpath', value='./td[3]').text)

    dict_football={'home': home,'score':score,'away':away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    time.sleep(2)
    return df_football


fifa = [get_misssing_data(year) for year in years]

driver.quit()

df_fifa = pd.concat(fifa)
df_fifa.to_csv('data/fifa_worldcup_missing_data.csv', index=False)






#____________________________________________

path = # Write your path here
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)


def get_misssing_data(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    driver.get(web)
    matches = driver.find_elements(by='xpath', value='//td[@align="right"]/.. | //td[@style="text-align:right;"]/..')
    # matches = driver.find_elements(by='xpath', value='//tr[@style="font-size:90%"]')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find_element(by='xpath', value='./td[1]').text)
        score.append(match.find_element(by='xpath', value='./td[2]').text)
        away.append(match.find_element(by='xpath', value='./td[3]').text)

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    time.sleep(2)
    return df_football


driver.quit()



years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018]

fifa = [get_misssing_data(year) for year in years]
driver.quit()
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv("fifa_worldcup_missing_data.csv", index=False)
