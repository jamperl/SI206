# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
import re
from bs4 import BeautifulSoup

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")

words = soup.find_all(text=True)
new_words = []
for txt in words:
	if re.search('student', txt):
		new_txt = re.sub('student', 'AMAZING student', txt)
		new_words.append(new_txt)
	else:
		new_words.append(txt)

for item in new_words:
	print (item, end=' ')

# images = soup.find_all('img')
# for img in images:
# 	if img.p:
# 		print (img)
