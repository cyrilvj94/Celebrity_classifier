

# Importing the essential libraries
from bs4 import BeautifulSoup
import requests
import os
from collections import defaultdict



def build_query(name, page):
    """
    function for building the query
    name: search name
    page: page no to be scrapped
    """
    return 'https://www.gettyimages.in/photos/{}?mediatype=photography&page={}&phrase={}&sort=mostpopular'.format(name,
                                                                                                                  page,
                                                                                                                  name)


def get_link(name, start_page, end_page):
    """
    Obtains the link of all images and stores in a dictionary with name as :param name
    :param name : name of player
    :param start page : start page to scrap
    :param n_pages: no of pages to scrap
    """
    links = defaultdict(list)
    page_no = start_page

    try:
        while page_no <= end_page:
            url = build_query(name, page_no)
            print(url)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html5lib')

            for index, tag in enumerate(soup.find_all('figure', class_='gallery-mosaic-asset__figure')):
                try:
                    links[name].append(tag.find('img')['src'])
                    print(index, end='#')
                except Exception as e:
                    print(e, tag, index, '\n')
            print('page {} completed'.format(page_no))
            page_no += 1
    except Exception as e:
        print(e, 'Serious error')

    return links


def get_image(links, name, directory ):
    """
    Saves the images in a file, link should be a dictionary with name as key
    :param links : links of each name obtained from get_links function
    :name name of the star , it should be a key in links
    :directory to store image Dataset/Train_set/ or Dataset/Test_set/
    """
    d = directory + '{}'.format(name) + '/'

    if not os.path.isdir(d):  # Create a new directory if it does not exists
        os.makedirs(d)
        print('New directory created')

    for index, link in enumerate(links[name]):
        try:
            # time.sleep(ri(3, 10, 1))
            r = requests.get(link)
            with open( d + '{}.jpg'.format(link.split('=')[-2]), 'wb') as f:
                f.write(r.content)
                print(index, end='#')
                if index % 100 == 0:
                    print('\n')
        except Exception as e:
            print(e, 'Error in obtaining the image for {} index {}'.format(name, index))

