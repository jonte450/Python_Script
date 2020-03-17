import sys
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader, PdfFileWriter

output = PdfFileWriter()
watermark = PdfFileReader(open('watermark.pdf','rb'))
ipdf = PdfFileReader(open('super.pdf','rb'))


for index in range(ipdf.getNumPages()):
	page = ipdf.getPage(index)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)


with open('watermark_pdf.pdf', 'wb') as f:
	output.write(f)