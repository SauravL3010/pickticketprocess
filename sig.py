from PyPDF2 import PdfFileMerger
merger = PdfFileMerger()
merger.append('four_pdfs.pdf', pages=(0, 3))
merger.write('result.pdf')
merger.close()