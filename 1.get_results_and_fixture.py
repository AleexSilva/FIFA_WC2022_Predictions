import pandas as pd
import requests

from bs4 import BeautifulSoup


# Test with 1 FIFA World Cup Edition (2014)

web = 'https://en.wikipedia.org/wiki/2014_FIFA_World_Cup'
response=requests.get(web)
#print(response.text)

content = response.text
soup = BeautifulSoup(content,'lxml')

# We found a class that is the same for every table that show the result
matches = soup.find_all('div',class_='footballbox')
# We just need 3 parameters:
# 1) Which country was home 
# 2) Which country was home
# 3) Which was the final score

home=[]
away=[]
score=[]

for match in matches:
    home.append(match.find('th',class_='fhome').get_text()) # we use the class "fhome" to extract home team
    score.append(match.find('th',class_='fscore').get_text()) # we use the class "fscore" to extract the score
    away.append(match.find('th',class_='faway').get_text()) # we use the class "faway" to extract away team

dict_football ={'home':home,'away':away,'score':score}

df = pd.DataFrame(dict_football)
df['year'] = 2014

# Applied to all editions (from 1930 to 2018)

years = [
    1930,1934,1938,1950,1958,1962,1966,1970,1974,1978,
    1982,1986,1990,1994,1998,2002,2006,2010,2014,2018
]

def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response=requests.get(web)

    content = response.text
    soup = BeautifulSoup(content,'lxml')

    matches = soup.find_all('div',class_='footballbox')

    home=[]
    away=[]
    score=[]
    
    for match in matches:
        home.append(match.find('th',class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())    

    dict_football ={'home':home,'away':away,'score':score}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football

# results: historical data
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('data/fifa_worldcup_historical_data.csv', index=False)

# fixture
df_fixture = get_matches(2022)
df_fixture.to_csv('data/fifa_worldcup_fixture.csv', index=False)
