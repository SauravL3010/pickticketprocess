import win32com.client as win
import os
from jsonMod import load_json, add_to_json, update_values 
from pathMod import paths, create_directory, enter_directory
from excelModHelpers import get_sheet, lst_unupdated_exl, return_emty_cell, fill_cell


def excel():
    '''
    temp_dict = all rows in excel sheet
    temp_lst = all data per orderNo

    how does the algorithm work:
    - loads the latest json_data
    - for each orderNo in json_data which is not updated on excel yet: # also updates if 'status' has been changed
        - make "isExcelUpdated" = True
        - fill all the cells with new data
        - get a new empty cell
    '''
    file_name = r"C:\Users\0235124\OneDrive - University of Waterloo\Desktop\signodeProjects\pdfParse\pyPDF2\python_code\STABLE CODE\test\master_pick_tickets\master_pick_tickets.json"

    temp_dict = {
            "orderNo" : "A",
            "status" : "B",
            "shipTo" : "C",
            "via" : "D",
            "dateReceived" : "E",
            "previousReprint" : "F",
            "previousPrintStatus" : "G",
            "friendly_name" : "H",
            "fileDirectory" : "I",
            "emailAttachment" : "J",
            }

    temp_lst = [
            "orderNo",
            "status",
            "shipTo",
            "via",
            "dateReceived",
            "friendly_name",
            "fileDirectory",
            "emailAttachment",
            "previousReprint",
            "previousPrintStatus",
    ]


    # for _ in range(2):
        #Updates in "Just Received" sheet
    c = return_emty_cell(file_name, temp_dict, temp_lst)

    for order in lst_unupdated_exl(file_name, "isExcelUpdated", False, "status", "Just Received"):
        # update_values(file_name, order, "isExcelUpdated", True)
        temp_state = fill_cell(temp_lst, temp_dict, file_name, order, c)
        if temp_state:
            update_values(file_name, order, "isExcelUpdated", True)
        c = return_emty_cell(file_name, temp_dict, temp_lst)

    #Updates in "Shipped" sheet
    c = return_emty_cell(file_name, temp_dict, temp_lst, c=2, sheet = get_sheet(sheet = "Shipped"))

    for order in lst_unupdated_exl(file_name, "status", "Shipped", "isShippedExcelUpdated", False):
        # update_values(file_name, order, "isShippedExcelUpdated", True)
        temp_state = fill_cell(temp_lst, temp_dict, file_name, order, c, sheet = get_sheet(sheet="Shipped"))
        if temp_state:
            update_values(file_name, order, "isShippedExcelUpdated", True)
        c = return_emty_cell(file_name, temp_dict, temp_lst, c=2, sheet = get_sheet(sheet = "Shipped"))

    #updates in "Billed" sheet
    c = return_emty_cell(file_name, temp_dict, temp_lst, c=2, sheet = get_sheet(sheet = "Billed"))

    for order in lst_unupdated_exl(file_name, "status", "Billed", "isBilledExcelUpdated", False):
        # update_values(file_name, order, "isBilledExcelUpdated", True)
        temp_state = fill_cell(temp_lst, temp_dict, file_name, order, c, sheet = get_sheet(sheet="Billed"))
        if temp_state:
            update_values(file_name, order, "isBilledExcelUpdated", True)
        c = return_emty_cell(file_name, temp_dict, temp_lst, c=2, sheet = get_sheet(sheet = "Billed"))

    

