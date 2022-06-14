import os
import webbrowser

# get paths to all pdfs in current directory and subdirectories
path ="./"
filePaths = []
for root, dirs, files in os.walk(path):
	for file in files:
		filePaths.append(os.path.join(root,file))

# filter list by elements that end with .pdf
pdfsList = [name for name in filePaths if name.endswith(".pdf")]

# open all pdfs in default browser
for pdf in pdfsList:
	webbrowser.open_new_tab(pdf)
