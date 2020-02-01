#!/usr/bin/python
# -*- coding: utf-8 -*-

# argparse: https://docs.python.org/3.3/library/argparse.html
# The argparse module makes it easy to write user-friendly command-line interfaces
import argparse

import modules

parser = argparse.ArgumentParser(description='Python Kontoauszug Analysierer')
parser.add_argument('-d', '--directory', help='Das Verzeichniss wo die Kontoauszüge als PDF liegen', required=True)

args = parser.parse_args()

pdfreader = modules.PDFReader(args)
firstPDF = pdfreader.getPDFList()
pdfreader.readPdf(firstPDF[0])

