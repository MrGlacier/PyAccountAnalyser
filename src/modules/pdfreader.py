# https://docs.python.org/3/library/glob.html
# The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order
import glob

# https://docs.python.org/3/library/os.html
# This module provides a portable way of using operating system dependent functionality.
import os

# PyPDF2: https://pythonhosted.org/PyPDF2/
# A Pure-Python library built as a PDF toolkit
import PyPDF2

import modules

class PDFReader:
    pdfDirectory = None
    pdfFilesInDirectory = []
    pageContent = []

    def __init__(self, args):
        if os.path.isdir(args.directory):
            self.pdfDirectory = args.directory
            self.readDirectory()
        else:
            print("Directory does not exist! - " + args.directory)

    def readDirectory(self):
        if self.pdfDirectory is not None:
            self.pdfFilesInDirectory = glob.glob(self.pdfDirectory + "*.pdf")
        else:
            print("Directory not set!")

    def readPdf(self, pdfPath):
        pdf_file = open(pdfPath, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        print("Das PDF '" + pdfPath + "' hat " + str(number_of_pages) + " Seiten\r\n")
        page_content = ''
        for page_number in range(number_of_pages):   # use xrange in Py2
            page = read_pdf.getPage(page_number)
            page_content += page.extractText()
        
        oneEntry = self.extractEntrys(page_content.encode('utf-8'))
        print(oneEntry)
        accountEntry = modules.AccountEntry.fromList(oneEntry)
        accountEntry.get

    def extractEntrys(self, pageContent):
        return ["Lastschrift", "21.02", "-21,99", "Theo Tester", "DE77630901000131234562", "Test Abbuchung"]

    def getPDFList(self):
        return self.pdfFilesInDirectory