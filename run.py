#!/usr/bin/python3

import PyPDF2

pdfFile = open('LPIC-course', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(pdfReader.numPages)
