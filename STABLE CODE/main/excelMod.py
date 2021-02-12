import win32com.client as win
import os
from jsonMod import load_json, add_to_json, update_values 
from pathMod import paths, create_directory, enter_directory

def lst_unupdated_exl(json_data):
    list_return = []
    for k, v in json_data.items():
        if v["isExcelUpdated"] == False:
            list_return.append(k)
    return list_return

def get_active_excel_sheet():
    active_exl = win.GetActiveObject('Excel.Application')
    active_wrkbk = active_exl.Workbooks(1)
    active_wrksht = active_wrkbk.Worksheets(1)
    return active_wrksht

def excel():

    temp_lst = [
            "orderNo",
            "status",
            "shipTo",
            "via",
            "dateReceived",
            "friendly_name",
            "fileDirectory",
            "emailAttachment",
    ]

    temp_dict = {
            "orderNo" : "A",
            "status" : "B",
            "shipTo" : "C",
            "via" : "D",
            "dateReceived" : "E",
            "friendly_name" : "F",
            "fileDirectory" : "G",
            "emailAttachment" : "H",
            }

    active_wrksht = get_active_excel_sheet()

    file_name = r"C:\Users\0235124\OneDrive - University of Waterloo\Desktop\signodeProjects\pdfParse\pyPDF2\python_code\STABLE CODE\test\master_pick_tickets\master_pick_tickets.json"
    temp_json = load_json(file_name)

    # excel algorithm
    c = 2
    while active_wrksht.Range(f"{temp_dict['orderNo']}{c}").Value != 0:
        update_values(file_name, 
                    active_wrksht.Range(f"{temp_dict['orderNo']}{c}").Value, 
                    "status", 
                    active_wrksht.Range(f"{temp_dict['status']}{c}").Value)
        c += 1
    else:
        for order in lst_unupdated_exl(temp_json):
            update_values(file_name, order, "isExcelUpdated", True)
            for i in temp_lst[1:]:
                try:
                    active_wrksht.Range(f"{temp_dict[i]}{c}").Value = temp_json[order][i]
                except:
                    active_wrksht.Range(f"{temp_dict[i]}{c}").Value = order
            c += 1

