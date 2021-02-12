from prettytable import PrettyTable
import os

def table():
    extraction_info = PrettyTable()
    extraction_info.field_names = ["pdf file name", "num of pages extracted"]
    return extraction_info

def prettyInfo(file, pages, extraction_info):
    '''
    file = emailed file (mail%^**&^%.pdy)
    pages = pages in file
    '''
    extraction_info.add_row([os.path.basename(file), pages])
    
def print_to_console(extraction_info):
    '''
    info = extraction_info
    '''
    print(extraction_info)