# Top-x-synergies
# CURRENTLY REVAMPING AND ADDING LOTS OF COOL STUFF 
![image](https://user-images.githubusercontent.com/64566855/227442824-c2058b21-eae0-45db-bcf8-90527ea9f943.png)

Basically an aggregator of the top traits used by top players in the game Teamfight Tactics.
The output list can be modified by both Region and Player count (starting from top1, times out after 1000 instances).
without using selenium to refresh, the output loads in 100x faster, but that data won't be updated to this moment.

Included are some examples of outputs.

To make this work you'll need to:
Install BeatifulSoup4:
>pip install beautifulsoup4

Install Selenium:
>pip install selenium

Install Firefox (lol):
>https://www.mozilla.org/en-CA/firefox/new/

Install geckodriver:
>https://github.com/mozilla/geckodriver/releases

Change the directories of:
ln26: the path of the output.
ln45: the path at which firefox is installed at
ln63: the path at which geckodriver is installed at

Optional Changes:
ln31: the region which is analyzed.
ln93: # of players to analyze.



