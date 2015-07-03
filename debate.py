import urllib.request
import random
import re
from bs4 import BeautifulSoup
import os
import sys

if sys.version_info[:3] < (3,2,0):
    print('Requires Python >= 3.2.0')
    sys.exit(1)

os.system('clear')

cdhtml = urllib.request.urlopen('http://circuitdebater.wikispaces.com/').read()
soup1 = BeautifulSoup(cdhtml,"html.parser")
orgpagelinks = soup1.find_all("a", {"class": "wiki_link"})	
while True:
	try:
		randsoup = BeautifulSoup(urllib.request.urlopen(random.choice(orgpagelinks)['href']).read(),"html.parser")
	except ValueError:
		try:
			randsoup = BeautifulSoup(urllib.request.urlopen("http://circuitdebater.wikispaces.com" + 		random.choice(orgpagelinks)['href']).read(),"html.parser")
		except:
			continue
	break

doclinks = randsoup.find_all('a',{"class":"filename"})
while not doclinks:
	try:
		randsoup = BeautifulSoup(urllib.request.urlopen(random.choice(orgpagelinks)['href']).read(),"html.parser")

	except:
		randsoup = BeautifulSoup(urllib.request.urlopen("http://circuitdebater.wikispaces.com" + random.choice(orgpagelinks)['href']).read(),"html.parser")
	doclinks = randsoup.find_all('a',{"class":"filename"})

flag = False
while flag == False:
	file = random.choice(doclinks)
	if '/file/view' in file['href']:
		debatecase = urllib.request.urlopen('http://circuitdebater.wikispaces.com' + file['href'])
		localfile = open(file['title'],'wb')
		localfile.write(debatecase.read())
		localfile.close()
		os.system('open ' + '\'' + file['title'] + '\'')
		flag = True
