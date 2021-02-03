import sys
import urllib.request
from bs4 import BeautifulSoup
from multiprocessing import Pool


def fetch_links(url):
    """Function that takes in a URL, outputs a list of links found on the page, and prints them."""
    # set up html parser
    try:
        web_url = urllib.request.urlopen(url)
        data = web_url.read()
        soup = BeautifulSoup(data, 'html.parser')
    except:
        # Likely an SSL error, can't open page HTML
        return None

    # print main page url
    print(url)

    # make a list of all the sublinks
    all_links = set()
    for link in soup.find_all('a'):
        link_str = str(link.get('href'))
        if link_str.startswith('http'):
            all_links.add(link_str)

    # print list of links
    for link in all_links:
        print('   ' + link)

    return all_links


if __name__ == '__main__':
    # get input URL
    if len(sys.argv) != 2:
        raise ValueError('Please add one URL')
    starting_url = str(sys.argv[1])

    # get sub links, then find links of subpage
    sub_links = fetch_links(starting_url)
    if not sub_links:
        raise ValueError('The URL inputted has security settings that dissallows the downloading of html')

    for i in sub_links:
        fetch_links(i)
