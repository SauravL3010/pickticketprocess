import win32com.client as win
from datetime import datetime
from datetime import date
import glob
import os
try:
    import re2 as re
except ImportError:
    import re
from PyPDF2 import PdfFileReader

ticket_dict = {'ship':'', 'via':''}

def mainData(data):
    pattern = re.compile(r'Order(.*)FOB')
    patternMatches = pattern.finditer(data)
    pickTicketData = [match for match in patternMatches] # text data
    return pickTicketData[0].group(0) # --> goes to via

def ship(data):
    pattern = re.compile(r'ShipTo(.*)Order ')
    patternMatches = pattern.finditer(data)
    pickTicketData = [match for match in patternMatches] # text data
    return pickTicketData[0].group(0)[6:-6]

def via(info): # --> mianData
    pattern = re.compile(r'Signode -(.*)Net')
    patternMatches = pattern.finditer(info)
    pickTicketData = [match for match in patternMatches]
    returnData = pickTicketData[0].group(0).replace('Signode -', '')
    returnData = returnData.replace('Net', '')
    return returnData

def loop(file):
    openPdf = open(file, "rb")
    inputPdf = PdfFileReader(openPdf)
    pageInfo = inputPdf.getPage(0)
    rawData = pageInfo.extractText()
    openPdf.close()
    rawData = re.sub(r'\r\n', ' ', rawData)
    main_data = mainData(rawData)
    ship_data = ship(rawData)
    viaInfo = via(main_data)
    ticket_dict['ship'] = ship_data
    ticket_dict['via'] = viaInfo

def add_to_excel():


    status = ["", "Just Received", "Picked", "Staged", "Shipped"]

    activeExcel = win.GetActiveObject('Excel.Application')

    excelWrkBk = activeExcel.Workbooks(1)

    excelWrkSts = excelWrkBk.Worksheets(1)

    today = date.today()
    files_path = r'C:\Users\0235124\OneDrive - University of Waterloo\Desktop\signodeProjects\pdfParse\pyPDF2\OneDrive' + '\\' + str(today) 
    os.chdir(files_path)

    pdf_files_to_add = glob.glob(os.path.join(files_path, '*.pdf'))

    ############# Check for valid cellNo (cell.Value == None), init value in the next empty cell
    init = 2
    valid = True
    pick_ticket_already_in_excel = []
    while valid:
        no = f'B{init}'
        if excelWrkSts.Range(no).Value == None:
            break
        pick_ticket_already_in_excel.append(excelWrkSts.Range(no).Value)
        init += 1
        
    ############ Now we have the init No
    for file in pdf_files_to_add:
        if os.path.basename(file[:-4]) in pick_ticket_already_in_excel:
            continue
        date_received = datetime.now() #1
        friendly_name = '"' + os.path.basename(file[:-4]) + '"'#2
        link_location = '"' + file + '"' #2
        target_cells = [f'A{init}', f'B{init}', f'C{init}', f'D{init}', f'E{init}']

        ############ Extract Info
        loop(file)

        excelWrkSts.Range(target_cells[0]).Value = date_received
        excelWrkSts.Range(target_cells[1]).Formula = f'=HYPERLINK({link_location}, {friendly_name})'
        excelWrkSts.Range(target_cells[2]).Value = ticket_dict['ship']
        excelWrkSts.Range(target_cells[3]).Value = ticket_dict['via']
        excelWrkSts.Range(target_cells[4]).Value = status[1]
        init += 1
        
    ############ Return to original path
    os.chdir('C:\\Users\\0235124\\OneDrive - University of Waterloo\\Desktop\\signodeProjects\\pdfParse\\pyPDF2\\OneDrive')

add_to_excel()

