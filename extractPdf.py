from PyPDF2 import PdfFileReader, PdfFileWriter
import os

# ================================== CONFIG ==================================
inputPath = './solutions'
outputPath = './extractedPages'
chosenPages = [1]
# ============================================================================


# create output directory if it does not exist
if not os.path.exists(outputPath):
    os.makedirs(outputPath)

# iterate over all files in input directory
for fileName in os.listdir(inputPath):
    pdf = PdfFileReader(inputPath + '/' + fileName)
    # choose pages from each file
    pdfWriter = PdfFileWriter()
    for page_num in chosenPages:
        pdfWriter.addPage(pdf.getPage(page_num))
    # write
    with open(outputPath + '/' + fileName, 'wb') as f:
        pdfWriter.write(f)

print('Extracted the pages', chosenPages, 'from the pdfs')