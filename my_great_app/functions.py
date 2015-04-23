__author__ = 'ben'

from bs4 import BeautifulSoup
import urllib.request as ur
import re


class story_nomodel(list):

    def __init__(self,headline,text,time):
        self.headline = headline
        self.text = text
        self.time = time

    def __str__(self):
        return self.headline + "\t" + self.time + "\n" + self.text

#soupifies a URL
def soup_from_address(address):
    page = ur.urlopen(address)
    my_soup = BeautifulSoup(page)
    return(my_soup)

#Takes a list of strings and concatenates them, removing html tags and excess blank space
def list_format(the_list):
    base = ""
    for item in the_list:
        to_add = str(item).strip()
        base = base + ' ' + to_add

    final_string = strip_replace_html(base)

    return(final_string)

#takes a string, removes html tags, and removes excess blank space
def strip_replace_html(my_string):
    temp_string = re.sub("<.*?>","",my_string)
    temp_string = re.sub("\s+"," ",temp_string)
    final_string = temp_string.strip()
    return(final_string)


def get_bb_headlines(soup):
    headlines = soup.find_all('h1',class_="search-result-story__headline")

    headline_tags = [hl.find('a') for hl in headlines]
    #list of headlines, which are themselves lists
    actual_headlines = [hl.contents for hl in headline_tags]

    formatted_headlines = []
    for hl in actual_headlines:
        headline_string = list_format(hl)
        formatted_headlines.append(headline_string)

    return(formatted_headlines)

def get_bb_stories(soup):
    stories = soup.find_all("div",class_="search-result-story__body")
    story_contents = [story.contents for story in stories]
    formatted_stories = []
    for item in story_contents:
        item_string = list_format(item)
        formatted_stories.append(item_string)

    return(formatted_stories)

def get_bb_times(soup):
    time_tags = soup.find_all('time',class_="published-at")

    times = [item.contents for item in time_tags]
    formatted_times = [item[0].strip() for item in times]

    return(formatted_times)

def bloomberg_stories(search_term,max_return=3):
    url_search = search_term.replace(" ","+")
    page = 'http://www.bloomberg.com/search?query=' + url_search + '&category=Articles'

    soup = soup_from_address(page)

    #check to see if there are any results
    no_results = soup.find("div",class_="content-no-results")

    #if there are results then go ahead
    if no_results is None:
        headlines = get_bb_headlines(soup)
        stories = get_bb_stories(soup)
        times = get_bb_times(soup)

        #the number of stories we have
        story_count = min(len(headlines),len(stories),len(times))

        max_stories = min(story_count,max_return)
        story_list = []
        for k in range(max_stories):
            curr_headline = headlines[k]
            curr_story = stories[k]
            curr_time = times[k]
            new_story = story_nomodel(curr_headline,curr_story,curr_time)
            story_list.append(new_story)

    else:#return none if no stories are found
        story_list = None

    return(story_list)