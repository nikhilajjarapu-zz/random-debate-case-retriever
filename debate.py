import urllib.request
import random
import re
from bs4 import BeautifulSoup
import os
import sys
import time
import string

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

print("Press enter when you start spreading. Press enter again once you are done. ")
input()
curr = time.time()
input()
end = time.time()
deb8time = end-curr
flagChanged = False
with open("debatetimes.txt","a+") as file2:
	for line in file2:
		if file['title'] + "," in line:
			oldarr = line.split(',',2) 
			print("Your old time for " + orldarr[0] + "was " + oldarr[1])
			if oldarr[1] > deb8time:
				print("You beat your record! Good job.")
				line = ','.join([file['title'],deb8time])
			else:
				print("You were faster before. Keep improving!")
			flagChanged = True
	if flagChanged == False:
		print("You haven't spread this case before.")
		newtime = input("What time did you get? MM:SS ")
		file2.write(','.join([file['title'],newtime]))
