import pytest
import requests
from bs4 import BeautifulSoup
from website import Website
from tools import (
    transfer_popularity, transfer_db, transfer_backend, transfer_frontend, transfer_websites, transfer_note)

websites_list = []


@pytest.fixture(scope='session', autouse=True)
def prepare_running():
    """
    Reading datas from table
    :return: 
    """
    url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

    resp = requests.get(url=url)

    page = BeautifulSoup(resp.content)
    table_c = page.find('table', attrs={'class': 'wikitable'}).find('tbody').findAll('tr')
    table = table_c[1:]

    for stroke in table:
        items = stroke.findAll('td')

        website = transfer_websites(website=items[0])
        popularity = transfer_popularity(popularity=items[1])
        front = transfer_frontend(frontend=items[2])
        back = transfer_backend(backend=items[3])
        database = transfer_db(database=items[4])
        notes = transfer_note(note=items[5])

        websites_list.append(Website(
            website=website,
            popularity=popularity,
            frontend=front,
            backend=back,
            database=database,
            notes=notes
        )
        )

@pytest.fixture()
def Websites():
    return websites_list
