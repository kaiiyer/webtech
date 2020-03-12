import requests
from bs4 import BeautifulSoup
from colorama import Fore

"""
Colorama handles the text display coloring. Follow same scheme and pattern for coherence.
Moreover, to add more methods write functions in the scraper class, and call them in webtech.py
under the "scraping" function.
"""

class Scraper():

    def __init__(self,url):

        self.url = url
        self.result = requests.get(self.url)
        self.src = self.result.content
        self.soup = BeautifulSoup(self.src, "html.parser")


    def display_title(self):

        print((Fore.LIGHTGREEN_EX + "Webpage: " + Fore.RESET) + (Fore.WHITE + self.soup.title.string + Fore.RESET))
        print("\n")

    def display_header(self):
        print(Fore.LIGHTGREEN_EX + "HEADER TAGS: " +  Fore.RESET + "\n")
        titles = self.soup.find_all(['h1' , 'h2', 'h3' , 'h4' , 'h5' , 'h6'])
        for i in titles:
            print(i)

        print("\n")

    def display_links(self):

        links = self.soup.find_all("a")
        print(Fore.LIGHTGREEN_EX + "LINKS: " +  Fore.RESET + "\n")
        for ind, val in enumerate(links):
            print((Fore.CYAN +  val.text +f"_link{ind+1}: " + Fore.RESET) + val.attrs["href"])

