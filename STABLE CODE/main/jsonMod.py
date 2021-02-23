import json 

def load_json(file_name):
    '''
    file_name = .json file
    '''
    with open(file_name, 'r') as read_file:
        try:
            loaded_data = json.load(read_file) # load master data
        except Exception as e:
            print(f'Error while loading json file error -- {e}')
    return loaded_data

def add_to_json(file_name, key, value):
    '''
    file_name = .json file
    key = "order_no" of the target file
    value = {
                    "dateReceived" : None,
                    "originalPrint" : None,
                    "reprintDate" : None,
                    "emailAttachment" : None,
                    "fileDirectory" : None,
                    "status" : None,
                    "isExcelUpdated" : None
            }
    
    1) open json file, load data, append new data
    2) open json file, dump/save the same data to json
    
    difference 'r' and 'w'
    
    data structure to add to dictionary: 
    "ordrNo" : {
                    "dateReceived" : None,
                    "originalPrint" : None,
                    "reprintDate" : None,
                    "emailAttachment" : None,
                    "fileDirectory" : None,
                    "status" : None,
                    "isExcelUpdated" : None
                }
    "ordrNo_reprint": {
                    "dateReceived" : None,
                    "originalPrint" : None,
                    "reprintDate" : None,
                    "emailAttachment" : None,
                    "fileDirectory" : None,
                    "status" : None,
                    "isExcelUpdated" : None
                }
    '''
    with open(file_name, 'r') as read_file:
        loaded_data = json.load(read_file) # load master data
        loaded_data[key] = value # append to master data
    
    with open(file_name, 'w') as write_file:
        json.dump(loaded_data, write_file, indent=4)
        
def update_values(file_name, key, update_key, value):
    '''
    file_name = .json file
    key = to find "order_no" in hashable dict
    update_key = from one of ["dateReceived",
                    "originalPrint",
                    "reprintDate",
                    "emailAttachment",
                    "fileDirectory",
                    "status",
                    "isExcelUpdated"], also used to add new (k, v) pairs within key 
    value = update value in (update_key, value) pair
    '''
    with open(file_name, 'r') as read_file:
        loaded_data = json.load(read_file) # load master data
        loaded_data[key][update_key] = value # append to master data
    
    with open(file_name, 'w') as write_file:
        json.dump(loaded_data, write_file, indent=4)