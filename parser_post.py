# ---------------------------------------------------------------
# This program shows how to search the first ten results from
# google website
# Written by Yingli Zhao, February 2022
# ---------------------------------------------------------------
import json
import traceback
import requests
from bs4 import BeautifulSoup


#   Anzeige im Googlesearch wird hier ausgeschlossen
def searchresults(keyword):
    """
    search the given keyword in google
    :param keyword: what will be searched
    :return: name of Json file
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}
    url = 'https://google.com/search'
    kv = {'q': keyword, 'start': '0', 'num': '20'}
    # Pass in parameters: search keyword, start from the first search result, 20 search results on one page
    try:
        re = requests.get(url, params=kv, headers=headers)
        re.encoding = re.apparent_encoding
        if re.status_code != 200:
            # bad response from website
            raise Exception('Statuscode of google is:' + str(re.status_code))
        else:
            content = BeautifulSoup(re.content, 'html.parser')
            # parse response to a BeautifulSoup object, using HTML parser
            elements = content.find_all("div", {"class": "yuRUbf"})
            # parse content to find certain HTML tag
            result = {}
            # dictionary to save the search results pair {title:link}
            if len(elements) <= 10:
                for i in range(len(elements)):
                    title = elements[i].find("h3", {"class": "LC20lb MBeuO DKV0Md"}).text
                    link = elements[i].find("a", href=True)['href']
                    key = 'Searchresult[' + str(i) + ']'
                    result[key] = [title, link]
            else:
                for i in range(10):
                    title = elements[i].find("h3", {"class": "LC20lb MBeuO DKV0Md"}).text
                    link = elements[i].find("a", href=True)['href']
                    key = 'Searchresult[' + str(i) + ']'
                    result[key] = [title, link]

        filename = "result_getMethode_2.json"
        # define output file name
        with open(filename, "w") as outfile:
            json.dump(result, outfile)
            # write dictionary to json file
        return filename

    except Exception as e:
        traceback.print_exc()
        return None
