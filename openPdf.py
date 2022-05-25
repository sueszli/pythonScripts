import os
import webbrowser

# Open up all pdfs in all subdirectories (in your default browser) 

path ="./"

filePaths = []
for root, dirs, files in os.walk(path):
	for file in files:
		filePaths.append(os.path.join(root,file))

# filter list by elements that end with .pdf
pdfsList = [name for name in filePaths if name.endswith(".pdf")]

for pdf in pdfsList:
	webbrowser.open_new_tab(pdf)
