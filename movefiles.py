import os
import glob
from datetime import date
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

today  = date.today()
ogpath = os.getcwd()
path = ogpath + '\\OneDrive - University of Waterloo\\' + str(today)

temp_set = ['7175649-00', '7182567-00']

for ticket in temp_set:
    old_name = path + '\\' + ticket + '.pdf'
    new_name = path + '\\' + ticket + ' (1).pdf'
    if os.path.exists(old_name) and not os.path.exists(new_name):
        os.rename(old_name, new_name)

    pdf_files = glob.glob(os.path.join(path,'*.pdf'))

    merge_these = []

    for file in pdf_files:
        if ticket in file:
            merge_these.append(file)

    merger = PdfFileMerger()

    for pdf in merge_these:
        merger.append(pdf)

    os.chdir(path)
    merger.write(f"{ticket}.pdf")
    os.chdir(ogpath)
    merger.close()

    for file in pdf_files:
        if ticket in file:
            if os.path.exists(file):
                os.remove(file)                                       

        



