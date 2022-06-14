import requests
from bs4 import BeautifulSoup
import os

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
for exam in exams:
    pdf = requests.get(url+exam)
    if not os.path.exists('exams'):
        os.makedirs('exams')
    file = open('exams/'+exam.replace('-pruefung.pdf', '.pdf'), 'wb')
    file.write(pdf.content)
    file.close()
print(checkmark, 'Downloaded all exams')
