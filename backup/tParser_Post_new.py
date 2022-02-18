from googlesearch import search


def searchresults(query):
    #   tld: domain
    #   num: number of search result pro page
    #   start: first result to retrieve
    #   stop: last result to retrieve
    for j in search(query, tld="de", num=10, stop=10, pause=2):
        print(j)


if __name__ == "__main__":
    searchresults('linkedin')
