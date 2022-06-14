import requests
from bs4 import BeautifulSoup
import os
import PyPDF2

# parse page
url = "https://dbai.tuwien.ac.at/education/ssd/pruefung/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
checkmark = u'\u2713'
print(checkmark, 'Reached website')

# scrape links
exams = []
solutions = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None:
        if href.endswith('-pruefung.pdf'):
            exams.append(href)
        if href.endswith('-muster.pdf'):
            solutions.append(href)
print(checkmark, 'Found', len(exams), 'exams')
print(checkmark, 'Found', len(solutions), 'exam solution')

# download exams
print('Downloading exams...')
folderName = 'exams'
if not os.path.exists(folderName):
    os.makedirs(folderName)
for exam in exams:
    pdf = requests.get(url+exam)
    path = folderName + '/' + exam
    file = open(path, 'wb')
    file.write(pdf.content)
    file.close()
print(checkmark, 'Downloaded all exams')

# extract date from pdf-text
def extractDateFromText(text):
    date = ''
    for line in text.split("\n"):
        if '184.705' in line:
            date = line.split('184.705',1)[1]
        if '181.135' in line:
            date = line.split('181.135',1)[1]
    if date == '':
        print('Date couldn\'t be found in ', exam)
        date = 'unknown'
    date = date.replace(' ', '')
    # make DD.MM.YYYY to YYYY.MM.DD
    elems = date.split('.')
    return elems[2] + '.' + elems[1] + '.' + elems[0]

# read and rename files
print('Changing names of exams to their dates...')
for exam in os.listdir(folderName):
    path = folderName + '/' + exam
    with open(path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = reader.pages[0].extract_text()
        date = extractDateFromText(text)
    newPath = folderName + '/' + date + '.pdf'
    if not os.path.exists(newPath):
        os.rename(path, newPath)
    else:
        alternativePath = folderName + '/' + date + '[V2]' + '.pdf'
        os.rename(path, alternativePath)
print(checkmark, 'Renamed all exams')
