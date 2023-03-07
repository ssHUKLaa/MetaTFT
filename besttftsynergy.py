<<<<<<< Updated upstream
import requests
from bs4 import BeautifulSoup
from collections import Counter
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import datetime
import time
 
#############################################################
#writes to file in accordiance with current date 
class Logger: 
 
    def __init__(self, filename):
        self.console = sys.stdout
        self.file = open(filename, 'w', encoding="utf-8")
 
    def write(self, message):
        self.console.write(message)
        self.file.write(message)
 
    def flush(self):
        self.console.flush()
        self.file.flush()
current_date = str(datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S'))
path = 'C:/Directory/to/change/besttftsynergy/' + current_date + '.txt'
sys.stdout = Logger(path)

#######################################################################

URL = "https://lolchess.gg/leaderboards?mode=ranked&region=na" #lets you know what site we're working with
page = requests.get(URL) #makes requests to the site

soup = BeautifulSoup(page.content, "html.parser") #simply gets all html information regarding the site

results = soup.find(id="wrapper") #looks for stuff in the <div: wrapper>

summoner_ids = results.find_all('td', {"class": "summoner"}) #finds all <td: summoner> tags in <div: wrapper>

player = 0
synergies = []
winning_synergies = []

firefoxOptions = Options() #goofy ahh options so my output isnt flooded with every warning under the sun
firefoxOptions.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' #because chrome was doing a little funny
firefoxOptions.add_argument('--no-sandbox')
firefoxOptions.add_argument("--headless")
firefoxOptions.add_argument("--log-level=3")
firefoxOptions.add_argument('--ignore-certificate-errors')
firefoxOptions.add_argument('--ignore-ssl-errors')
firefoxOptions.add_argument('--disable-dev-shm-usage')

for summoner_id in summoner_ids: #gets specific elements from summoner class
        summoner_rank = summoner_id.find('span', {"class": "rank"}) #finds specific classes in div summoner
        summoner_name = summoner_id.find('a')
        summoner_link = summoner_id.find('a')['href']
        summoner = str(summoner_name.text) #turns summoner_name.text into a string
        print("rank" + summoner_rank.text,end="\n")
        print(summoner.strip(),end="\n")
        print(summoner_link,end="\n")
        page2 = requests.get(summoner_link) #requests player page
        player_page = BeautifulSoup(page2.content, "html.parser") #does parsing
        driver = webdriver.Firefox(executable_path=r'D:\Other Programs\driver\geckodriver.exe', options=firefoxOptions) #initializes a firefox app
        driver.set_page_load_timeout(12000)
        driver.get(summoner_link) #gets link for selenium
        refresh_history = driver.find_element_by_id("btn-update") #finds "refresh" button
        refresh_history.click() #clicks button
        time.sleep(5) #waits 5 seconds to allow for refresh
        matches = player_page.find(id="wrapper") #looks for stuff in the <id: wrapper>
        match_history = matches.select('div[class*="profile__match-history-v2__item placement"]') #finds any <div> that fufills having the class words profile__match-history-v2__item placement
        Game = 0

        for matches in match_history: #lists matches
            placement = matches.find('div', class_="placement")
            number_of_placement = int("".join(filter(str.isdigit, placement.text)))
            all_traits = matches.select('div[class*="tft-hexagon-image tft-hexagon-image--black tft-hexagon-image"]') #finds any <div> that fufills having the class name tft-hexagon-image tft-hexagon-image--black tft-hexagon-image
            Game += 1
            print("Game: " + str(Game),end="\n")
            print("placement " + placement.text,end="\n")

            for all_trait in all_traits: #lists traits
                trait = all_trait.find('img')['alt'] #looks for alt class name under <img>
                print(trait + "\n",end="")
                number_of_trait = int("".join(filter(str.isdigit, trait))) #gets number of units in a synergy

                if number_of_trait >= 3:
                    synergies.append(trait) #adds to list named synergies if less than/equal to 3 traits
                if (number_of_placement <=4) and (number_of_trait >= 3):
                    winning_synergies.append(trait) #adds to list named winning_synergies
                
            print(" ",end="\n")
        player += 1
        if player == 10: #decides sample size of top players, max is 100
            break
        driver.quit()

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0] #finds most common synergy
print(synergies)
print(winning_synergies)
print("Most frequent synergy: " + most_frequent(synergies))
print("Most frequent winning synergy: " + most_frequent(winning_synergies))
print(len(synergies))
=======
import requests
from bs4 import BeautifulSoup
from collections import Counter
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import datetime
import time
 
#############################################################
#writes to file in accordiance with current date 
class Logger: 
 
    def __init__(self, filename):
        self.console = sys.stdout
        self.file = open(filename, 'w', encoding="utf-8")
 
    def write(self, message):
        self.console.write(message)
        self.file.write(message)
 
    def flush(self):
        self.console.flush()
        self.file.flush()
current_date = str(datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S'))
path = 'C:/Directory/to/change/besttftsynergy/' + current_date + '.txt'
sys.stdout = Logger(path)

#######################################################################

URL = "https://lolchess.gg/leaderboards?mode=ranked&region=na" #lets you know what site we're working with
page = requests.get(URL) #makes requests to the site

soup = BeautifulSoup(page.content, "html.parser") #simply gets all html information regarding the site

results = soup.find(id="wrapper") #looks for stuff in the <div: wrapper>

summoner_ids = results.find_all('td', {"class": "summoner"}) #finds all <td: summoner> tags in <div: wrapper>

player = 0
synergies = []
winning_synergies = []

firefoxOptions = Options() #goofy ahh options so my output isnt flooded with every warning under the sun
firefoxOptions.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' #because chrome was doing a little funny
firefoxOptions.add_argument('--no-sandbox')
firefoxOptions.add_argument("--headless")
firefoxOptions.add_argument("--log-level=3")
firefoxOptions.add_argument('--ignore-certificate-errors')
firefoxOptions.add_argument('--ignore-ssl-errors')
firefoxOptions.add_argument('--disable-dev-shm-usage')

for summoner_id in summoner_ids: #gets specific elements from summoner class
        summoner_rank = summoner_id.find('span', {"class": "rank"}) #finds specific classes in div summoner
        summoner_name = summoner_id.find('a')
        summoner_link = summoner_id.find('a')['href']
        summoner = str(summoner_name.text) #turns summoner_name.text into a string
        print("rank" + summoner_rank.text,end="\n")
        print(summoner.strip(),end="\n")
        print(summoner_link,end="\n")
        page2 = requests.get(summoner_link) #requests player page
        player_page = BeautifulSoup(page2.content, "html.parser") #does parsing
        driver = webdriver.Firefox(executable_path=r'D:\Other Programs\driver\geckodriver.exe', options=firefoxOptions) #initializes a firefox app
        driver.set_page_load_timeout(12000)
        driver.get(summoner_link) #gets link for selenium
        refresh_history = driver.find_element_by_id("btn-update") #finds "refresh" button
        refresh_history.click() #clicks button
        time.sleep(5) #waits 5 seconds to allow for refresh
        matches = player_page.find(id="wrapper") #looks for stuff in the <id: wrapper>
        match_history = matches.select('div[class*="profile__match-history-v2__item placement"]') #finds any <div> that fufills having the class words profile__match-history-v2__item placement
        Game = 0

        for matches in match_history: #lists matches
            placement = matches.find('div', class_="placement")
            number_of_placement = int("".join(filter(str.isdigit, placement.text)))
            all_traits = matches.select('div[class*="tft-hexagon-image tft-hexagon-image--black tft-hexagon-image"]') #finds any <div> that fufills having the class name tft-hexagon-image tft-hexagon-image--black tft-hexagon-image
            Game += 1
            print("Game: " + str(Game),end="\n")
            print("placement " + placement.text,end="\n")

            for all_trait in all_traits: #lists traits
                trait = all_trait.find('img')['alt'] #looks for alt class name under <img>
                print(trait + "\n",end="")
                number_of_trait = int("".join(filter(str.isdigit, trait))) #gets number of units in a synergy

                if number_of_trait >= 3:
                    synergies.append(trait) #adds to list named synergies if less than/equal to 3 traits
                if (number_of_placement <=4) and (number_of_trait >= 3):
                    winning_synergies.append(trait) #adds to list named winning_synergies
                
            print(" ",end="\n")
        player += 1
        if player == 10: #decides sample size of top players, max is 100
            break
        driver.quit()

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0] #finds most common synergy
print(synergies)
print(winning_synergies)
print("Most frequent synergy: " + most_frequent(synergies))
print("Most frequent winning synergy: " + most_frequent(winning_synergies))
print(len(synergies))
>>>>>>> Stashed changes
print(len(winning_synergies)) #prints everything we need 