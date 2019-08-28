#! python3
# lucky.py -> open several google search results

import requests,sys,webbrowser,bs4

print('Googling') # displaying text while downloading

res = requests.get('https://www.google.com/search?q=BeautifulSoap') #.join(sys.argv[1]))
res.raise_for_status()

# Receive Top results links
# soup = bs4.BeautifulSoup(res.text)
# open browser tab for each results
# linkElems = soup.select('.r a')
# print(soup)

soup = bs4.BeautifulSoup(res.content,'html.parser')
print(soup)

