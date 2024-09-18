from bs4 import BeautifulSoup
import requests

def get_crime(state_code, city):

    url = "https://www.neighborhoodscout.com/" + state_code + "/" + city + "/crime"
    
    site = requests.get(url).text

    soup = BeautifulSoup(site, 'lxml')

    s = soup.find('h1', 'score').text

    crime_score = ''

    for a in s:
        if a != '\n':
            crime_score += a

    return crime_score

def get_housing_market(state_code, city):

    url = "https://www.neighborhoodscout.com/" + state_code + "/" + city + "/real-estate"

    site = requests.get(url).text

    soup = BeautifulSoup(site, 'lxml')

    s = soup.find('p', class_='report-card-text text-center text-cl-black text-2xl font-weight-semi-bold mt-2 mb-0').text

    housing_cost = ''

    for a in s:
        if a != '\n':
            housing_cost += a

    return housing_cost