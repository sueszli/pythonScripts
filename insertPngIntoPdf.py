from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import webbrowser

# ============================ configure ============================
inputPath = 'input.pdf'
outputPath = 'output.pdf'
imgPath = 'logo.png'
tempPath = 'temp.pdf'
imgSize = 70
x = 500
y = 760
# ====================================================================

# Create temporary pdf and position image in it
c = canvas.Canvas(tempPath)
c.drawImage(imgPath, x, y, width=imgSize, height=imgSize)
c.save()

# read
tempFile = PdfFileReader(open(tempPath, "rb")).getPage(0)
outputFile = PdfFileWriter()
inputFile = PdfFileReader(open(inputPath, "rb"))

# merge onto every page from input
for i in range(inputFile.getNumPages()):
    page = inputFile.getPage(i)
    page.mergePage(tempFile)
    outputFile.addPage(page)

with open(outputPath, "wb") as out:
    outputFile.write(out)

# open pdf in default browser
webbrowser.open(outputPath)
