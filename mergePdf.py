from PyPDF2 import PdfFileMerger
import os

# ================================== CONFIG ==================================
inputPath = './extractedPages'
# ============================================================================


total = len(os.listdir(inputPath))
count = 1
merger = PdfFileMerger()
for pdf in os.listdir(inputPath):
    merger.append(open(inputPath + '/' + pdf, 'rb'))
    print('merged [' + str(count) + '/' + str(total) + '] ...', pdf)
    count += 1

with open('merged.pdf', "wb") as out:
    merger.write(out)

print('Merged all pages')
