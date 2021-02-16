import win32com.client as win
from jsonMod import load_json, add_to_json, update_values 
from datetime import datetime

import win32com.client as win

def get_sheet(sheet, file = "testfile.xlsx"):
    '''
    sheet = sheet name
    file = default is 'main excel file', optional
    
    returns excel worksheet
    '''
    return_obj = None
    book = None
    for i in range(10):
        try:
            if win.GetActiveObject("Excel.Application").Workbooks(i).Name == file:
                return_obj = win.GetActiveObject("Excel.Application").Workbooks(i)
                book = i
                break
        except:
            continue
    for i in range(10):
        try:
            if win.GetActiveObject("Excel.Application").Workbooks(book).Worksheets(i).name == sheet:
                return_obj = win.GetActiveObject("Excel.Application").Workbooks(book).Worksheets(i)
                sheet = i
        except:
            continue
    return return_obj

def lst_unupdated_exl(json_file, var, value, var1=None, value1=None):
    '''
    json_data = loaded json data (load everytime before calling this function)
    
    returns a list of ["isExcelUpdated"] == False OrderNo's
    '''
    json_data = load_json(json_file)
    list_return = []
    for k, v in json_data.items():
        if var1 == None and value1 == None:
            if v[var] == value:
                list_return.append(k)
        else:
            if v[var] == value and v[var1] == value1:
                list_return.append(k)
    return list_return

def return_emty_cell(file_name, temp_dict, temp_lst, c=2, sheet = get_sheet(sheet = "Just Received")):
    # moved_is_found = False
    # moved_c = 0

    while sheet.Range(f"{temp_dict['orderNo']}{c}").Value != 0:
        # must be a valid order no. 
        # if moved is found, change return c:
        # if sheet.Range(f"{temp_dict['orderNo']}{c}").Value == "moved":
        #     moved_is_found = True
        #     moved_c = c


        update_values(file_name, 
                      sheet.Range(f"{temp_dict['orderNo']}{c}").Value, 
                      "status", 
                      sheet.Range(f"{temp_dict['status']}{c}").Value)
        
        order = sheet.Range(f"{temp_dict['orderNo']}{c}").Value
        move_cells(temp_lst, temp_dict, file_name, order, sheet, c)
        
        # find the first 0 or first "moved":
        # 
        c += 1
        # return_c = c
        # return_c = c
        # if moved_is_found:
        #     return_c = moved_c
    return c

def fill_cell(temp_lst, temp_dict, json_file, order, c, sheet = get_sheet(sheet="Just Received")):
    temp_json = load_json(json_file)
    for i in temp_lst[1:]:
        try:
            sheet.Range(f"{temp_dict[i]}{c}").Value = temp_json[order][i]
        except:
            if i == "friendly_name":
                sheet.Range(f"{temp_dict[i]}{c}").Value = order
    reprints(json_file, temp_dict, order, c, sheet)
                
def reprints(json_file, temp_dict, order, c, sheet=get_sheet(sheet = "Just Received")):
    temp_json = load_json(json_file)
    if temp_json[order]["originalPrint"] == False:
        previous_order = "_".join('7175649-00_reprint'.split("_")[:-1])
        friendly_name = '"' + previous_order + '"'
        link_location = '"' + temp_json[previous_order]["fileDirectory"] + '"'
        status = temp_json[previous_order]["status"]
        formula = f'=HYPERLINK({link_location}, {friendly_name})'
        cell_range = f"{temp_dict['previousReprint']}{c}" 
        sheet.Range(cell_range).Formula = formula
        cell_range = f"{temp_dict['previousPrintStatus']}{c}"
        sheet.Range(cell_range).Value = status


def move_cells(temp_lst, temp_dict, file_name, order, sheet, c):
    json_data = load_json(file_name)
    
    # for sheet "Just Received"
    if sheet.Name == "Just Received":
        # user entered "Shipped"
        if json_data[order]["status"] == "Shipped":
            update_values(file_name, 
                          order, 
                          "shippedDate", 
                            str(datetime.now()))
            update_values(file_name, 
                          order,
                         "isExcelUpdated",
                         False)
            update_values(file_name, 
                         order, 
                         "isBilledExcelUpdated",
                         False)
            for i in temp_lst[1:]:
                try:
                    if i == "shipTo":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = "Moved to 'Shipped'"
                    elif i == "via":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = sheet.Range(f"{temp_dict['orderNo']}{c}").Value
                    else:
                        sheet.Range(f"{temp_dict[i]}{c}").Value = None
                except:
                    print("cannot empty cells")
                    
        # user entered "Billed"
        if json_data[order]["status"] == "Billed":
            update_values(file_name, 
                          order, 
                          "billedDate", 
                            str(datetime.now()))
            update_values(file_name, 
                          order,
                         "isExcelUpdated",
                         False)
            update_values(file_name, 
                         order, 
                         "isShippedExcelUpdated",
                         False)
            for i in temp_lst[1:]:
                try:
                    if i == "shipTo":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = "Moved to 'Billed'"
                    elif i == "via":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = sheet.Range(f"{temp_dict['orderNo']}{c}").Value
                    else:
                        sheet.Range(f"{temp_dict[i]}{c}").Value = None
                except:
                    print("cannot empty cells")
    
    # for sheet "Shipped"
    elif sheet.Name == "Shipped":
        # user entered "Billed"
        if json_data[order]["status"] == "Billed":
            update_values(file_name, 
                          order, 
                          "billedDate", 
                            str(datetime.now()))
            update_values(file_name, 
                          order,
                         "isExcelUpdated",
                         False)
            update_values(file_name, 
                         order, 
                         "isShippedExcelUpdated",
                         False)
            for i in temp_lst[1:]:
                try:
                    if i == "shipTo":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = "Moved to 'Billed'"
                    elif i == "via":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = sheet.Range(f"{temp_dict['orderNo']}{c}").Value
                    else:
                        sheet.Range(f"{temp_dict[i]}{c}").Value = None
                except:
                    print("cannot empty cells")
            
        # user entered "Just Received"
        if json_data[order]["status"] == "Just Received":
            update_values(file_name, 
                          order, 
                          "shippedDate", 
                            None)
            update_values(file_name, 
                          order,
                         "isBilledExcelUpdated",
                         False)
            update_values(file_name, 
                         order, 
                         "isShippedExcelUpdated",
                         False)
            for i in temp_lst[1:]:
                try:
                    if i == "shipTo":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = "Moved back to 'Just Received'"
                    elif i == "via":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = sheet.Range(f"{temp_dict['orderNo']}{c}").Value
                    else:
                        sheet.Range(f"{temp_dict[i]}{c}").Value = None
                except:
                    print("cannot empty cells")
    
    # for sheet "Billed"
    elif sheet.Name == "Billed":
        # user entered "Shipped"
        if json_data[order]["status"] == "Shipped":
            update_values(file_name, 
                          order, 
                          "billedDate", 
                            None)
            update_values(file_name, 
                          order,
                         "isExcelUpdated",
                         False)
            update_values(file_name, 
                         order, 
                         "isBilledExcelUpdated",
                         False)
            for i in temp_lst[1:]:
                try:
                    if i == "shipTo":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = "Moved back to 'Shipped'"
                    elif i == "via":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = sheet.Range(f"{temp_dict['orderNo']}{c}").Value
                    else:
                        sheet.Range(f"{temp_dict[i]}{c}").Value = None
                except:
                    print("cannot empty cells")
            
        # user entered "Just Received"
        if json_data[order]["status"] == "Just Received":
            update_values(file_name, 
                          order, 
                          "billedDate", 
                            None)
            update_values(file_name, 
                          order, 
                          "shippedDate", 
                            None)
            update_values(file_name, 
                          order,
                         "isBilledExcelUpdated",
                         False)
            update_values(file_name, 
                         order, 
                         "isShippedExcelUpdated",
                         False)
            for i in temp_lst[1:]:
                try:
                    if i == "shipTo":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = "Moved back to 'Just Received'"
                    elif i == "via":
                        sheet.Range(f"{temp_dict[i]}{c}").Value = sheet.Range(f"{temp_dict['orderNo']}{c}").Value
                    else:
                        sheet.Range(f"{temp_dict[i]}{c}").Value = None
                except:
                    print("cannot empty cells")