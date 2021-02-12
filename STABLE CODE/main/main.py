# import json 
# from datetime import date, datetime
import os
# import glob
# from PyPDF2 import PdfFileWriter, PdfFileReader
# try:
#     import re2 as re
# except ImportError:
#     import re
# from prettytable import PrettyTable

from jsonMod import load_json, add_to_json, update_values 
from pathMod import paths, create_directory, enter_directory, verify_directory, move_files
from algorithm import read_file
# from algoHelpers import reprint_dates, if_order_as_originalPrint, if_order_exists_return_renamed, append_data, ship_via
# from patternMod import find_pattern
from prettyinfo import table, prettyInfo, print_to_console
from allFiles import list_of_files



# file = "pick_ticket_6_pages_plus_pick_ticket_5_pages_plus_pick_ticket_2_pages_plus_two_pdf_file_only_1.pdf"
# jsonfile = "testfile.json"

# json_data = load_json(jsonfile)

# read_file(file, json_data, jsonfile, extraction_info)

def main():
    temp_path = paths(r"C:\Users\0235124\OneDrive - University of Waterloo\Desktop\signodeProjects\pdfParse\pyPDF2\python_code\STABLE CODE\test")
    code_path = r"C:\Users\0235124\OneDrive - University of Waterloo\Desktop\signodeProjects\pdfParse\pyPDF2\python_code\STABLE CODE\main"

    if os.getcwd() != temp_path["root_path"]:
        enter_directory(temp_path["root_path"])

    if not (verify_directory(temp_path["pick_ticket_path"]) and verify_directory(temp_path["email_archive"])):
        create_directory(temp_path["pick_ticket_path"])
        create_directory(temp_path["email_archive"])
        
    extraction_info = table()

    jsonfile = r"master_pick_tickets.json"

    all_files = list_of_files(temp_path["root_path"])

    for file in all_files:

        if os.getcwd() != temp_path["pick_ticket_path"]:
            enter_directory(temp_path["pick_ticket_path"])

        json_data = load_json(jsonfile)
        move_to = temp_path["email_archive"] + rf"\{os.path.basename(file)}"
        
            
        read_file(file, json_data, jsonfile, extraction_info, move_to)
        
        if os.getcwd() != temp_path["root_path"]:
            enter_directory(temp_path["root_path"])
        
        move_files(file, move_to)
        
    print_to_console(extraction_info)


    if os.getcwd() != code_path:
        enter_directory(code_path)



