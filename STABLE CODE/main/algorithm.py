from PyPDF2 import PdfFileWriter, PdfFileReader
from patternMod import find_pattern
from algoHelpers import reprint_dates, if_order_as_originalPrint, if_order_exists_return_renamed, append_data, ship_via
from datetime import datetime
from jsonMod import load_json, add_to_json, update_values 
from prettyinfo import table, prettyInfo, print_to_console
import os

def read_file(file, json_data, jsonfile, extraction_info, move_to):
    '''
    file = emailed file (mail%^**&^%.pdf)
    json_data = loaded json data (load everytime before calling this function)
    jsonfile = main json file ("master_pick_tickets.json")
    
    orders_dict = tracks the indices of page(s) this function has to extract from file
    json_dict_to_add = for each file json data for all picktickets is loaded only once and then appended to jsonfile
    
    data extracted form each page:
    {
        originalPrint, 
        reprintDate, 
        dateReceived, 
        emailAttachment, 
        shipTo, 
        via, 
        fileDirectory, 
        status = "Just Received", 
        shippedDate = None,
        billedDate = None,
        isExcelUpdated = False
        isShippedExcelUpdated = False,
        isBilledExcelUpdated = False,
    }
    
    if order_no already exists in previous email attachment, then "_reprint" is appended to order_no ("7182345-00_reprint")
    '''
    orders_dict = {}
    json_dict_to_add = {}
    with open(file, 'rb') as readfile:
        input_file = PdfFileReader(readfile)
        pages = input_file.numPages

        
        for page in range(pages):
            file_writer = PdfFileWriter()
            get_page = input_file.getPage(page)
            
            reprintDate = None
            master_text = get_page.extractText()
            narrowed_text = find_pattern(r'Order(.*)FOB', master_text)
            
            order_no = find_pattern(r'(\d{4,7})[-](\d{2})', narrowed_text)
            originalPrint = True
            if if_order_as_originalPrint(order_no, json_data):
                order_no = if_order_exists_return_renamed(order_no, json_data)
                reprint_dates(order_no, jsonfile, json_dict_to_add, json_data)
                originalPrint = False
            
            dateReceived = str(datetime.now())
            emailAttachment = move_to
            
            shipTo = find_pattern(r"ShipTo(.*)Order", master_text)[8:].split(" ")[:3]
            shipTo = " ".join(shipTo)
            
            via = ship_via("ALL_SHIP_VIA.json", narrowed_text)
            
            fileDirectory = os.getcwd() + rf"\{order_no}.pdf"
            
            try:
                orders_dict[order_no].append(page)
            except:
                orders_dict[order_no] = []
                orders_dict[order_no].append(page)
            
            for each_page in orders_dict[order_no]:
                file_writer.addPage(input_file.getPage(each_page))
                
            with open(f"{order_no}.pdf", "wb") as f:
                file_writer.write(f)
                f.close()
                
            ######## Adding data
            try:
                json_dict_to_add[order_no] = append_data(originalPrint, 
                                                         reprintDate, 
                                                         dateReceived, 
                                                         emailAttachment, 
                                                         shipTo, 
                                                         via,
                                                        fileDirectory)
            except:
                print("could not add data")
                
        for k, v in json_dict_to_add.items():
            add_to_json(jsonfile, k, v)
            
        prettyInfo(file, pages, extraction_info)