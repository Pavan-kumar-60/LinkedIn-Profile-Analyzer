# importing libraries
import os
import requests
from dotenv import load_dotenv


def scrape_linkedin_profile(l_url:str, mock: bool = False):
    
    if mock:
        linkedin_profile_url = 'https://gist.githubusercontent.com/Pavan-kumar-60/79423a7c5d1cc0767bec0fb3b3b961a5/raw/4068b0ba7b0e36b37ab610a5bc6afef8c4c95edf/Pavan-kumar-scraping'
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = 'https://api.scrapin.io/enrichment/profile'
        params ={
            'apikey': os.environ['SCRAPIO_API_KEY'],
            'linkedInUrl': l_url
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )
    data = response.json().get('person')
    return data