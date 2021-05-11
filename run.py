#!/usr/bin/python3

import PyPDF2
import os

pdfFiles = []

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

print(pdfFiles)

pdfFile = open(pdfFiles[0], 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(f'pages:{pdfReader.numPages}')

print(f'is encrypted:{pdfReader.isEncrypted}')

#print(pdfReader.getPage(0))
