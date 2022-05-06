import os
import webbrowser

path ="./"

filePaths = []
for root, dirs, files in os.walk(path):
	for file in files:
		filePaths.append(os.path.join(root,file))

# filter list by elements that end with .pdf
pdfsList = [name for name in filePaths if name.endswith(".pdf")]

for pdf in pdfsList:
	webbrowser.open_new_tab(pdf)