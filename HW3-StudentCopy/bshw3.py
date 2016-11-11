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

f = open('bshw3.html', 'w') # open new html file to write called bshw3
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')

words = soup.find_all(text=re.compile('student')) # create list of all sentences with the word student

for item in words:
	new_txt = re.sub('student', 'AMAZING student', item) # iterate through words and make new_txt = the new sentence with AMAZING before student
	item.replace_with(new_txt) # replace the original sentence with new_txt on the page

images = soup.find_all('img') # find all img tags
for img in images:
	if img['src'] == 'logo2.png': 
		img['src'] = 'media/logo.png' # if it is a michigan logo, replace with given SI logo in media folder
	else:
		img['src'] = 'media/leafs.jpg' # replace all other photos (the main photo) with a picture of myself

nice = soup.prettify()
f.write(nice) # write the new file with well formatted code
f.close() # close the file 


