import requests
from bs4 import BeautifulSoup
import os
import PyPDF2

# ================================== CONFIG ==================================
examDirectoryPath = './exams'
solutionDirectoryPath = './solutions'
# ============================================================================


# parse page
url = "https://dbai.tuwien.ac.at/education/ssd/pruefung/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
checkmark = u'\u2713'
print(checkmark, 'Reached website')


# scrape links
examLinks = []
solutionLinks = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None:
        if href.endswith('-pruefung.pdf'):
            examLinks.append(href)
        if href.endswith('-muster.pdf'):
            solutionLinks.append(href)
print(checkmark, 'Found', len(examLinks), 'exams')
print(checkmark, 'Found', len(solutionLinks), 'exam solution')


def downloadPdf(folderName, list):
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    for elem in list:
        pdf = requests.get(url + elem)
        path = folderName + '/' + elem
        file = open(path, 'wb')
        file.write(pdf.content)
        file.close()


print('Downloading exams...')
downloadPdf(examDirectoryPath, examLinks)
print(checkmark, 'Downloaded all exams')


print('Downloading solutions...')
downloadPdf(solutionDirectoryPath, solutionLinks)
print(checkmark, 'Downloaded all solutions')


def extractDateFromText(text, elem):
    date = ''
    for line in text.split("\n"):
        if '184.705' in line:
            date = line.split('184.705', 1)[1]
        if '181.135' in line:
            date = line.split('181.135', 1)[1]
    if date == '':
        print('Date couldn\'t be found in ', elem)
        date = 'unknown'
    date = date.replace(' ', '')
    # make DD.MM.YYYY to YYYY.MM.DD
    elems = date.split('.')
    return elems[2] + '.' + elems[1] + '.' + elems[0]


def rename(directoryPath):
    for elem in os.listdir(directoryPath):
        path = directoryPath + '/' + elem
        with open(path, 'rb') as file:
            text = PyPDF2.PdfFileReader(file).pages[0].extract_text()
            date = extractDateFromText(text, elem)
        newPath = directoryPath + '/' + date + '.pdf'
        # rename file (add '[V2]' to the end of the file name if it already exists)
        if not os.path.exists(newPath):
            os.rename(path, newPath)
        else:
            alternativePath = directoryPath + '/' + date + '[V2]' + '.pdf'
            os.rename(path, alternativePath)


print('Changing names of exams to their dates...')
rename(examDirectoryPath)
print(checkmark, 'Renamed all exams')


print('Changing names of solutions to their dates...')
rename(solutionDirectoryPath)
print(checkmark, 'Renamed all solutions')
